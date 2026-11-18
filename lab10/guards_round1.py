"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("Không có chính sách có hiệu lực tại ngày xử lý")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault"):
        return Verdict.allow()

    order = ctx.tools.lookup_order(action.get("order_id"))
    if order is None or order["customer_id"] != ctx.ticket.get("customer_id"):
        return Verdict.escalate("Không xác minh được đơn hàng và chủ đơn")
    if order["order_id"] != ctx.ticket.get("order_id"):
        return Verdict.escalate("Hành động ghi không thuộc đơn hàng của ticket")
    if action.get("ticket_id") != ctx.ticket.get("ticket_id"):
        return Verdict.escalate("Hành động ghi không thuộc ticket đang xử lý")

    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None or not order.get("parcels"):
        return Verdict.escalate("Thiếu chính sách hoặc dữ liệu kiện hàng để kiểm chứng")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)

    if tool == "issue_refund":
        # Check the ledger again before each write, including a retry.
        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            return Verdict.deny("Đơn đã có khoản hoàn trong sổ cái, chặn ghi lặp")

        amount = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if amount <= 0:
            return Verdict.deny("Tracking DB và chính sách không cho phép hoàn tiền")

        approval_id = action.get("approval_id")
        if amount > policy["auto_limit_vnd"] or approval_id:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id)
            approval = next((item for item in approvals if
                             item.get("ticket_id") == ctx.ticket["ticket_id"]
                             and item.get("order_id") == order["order_id"]
                             and item.get("customer_id") == order["customer_id"]
                             and item.get("status") == "valid"
                             and item.get("expires_at", "") >= ctx.as_of
                             and item.get("max_vnd", 0) >= amount), None)
            if approval is None or ctx.tools.ledger_rows(approval_id=approval_id):
                return Verdict.escalate("Khoản hoàn cần phê duyệt còn hiệu lực, đúng đối tượng và chưa dùng")

        if action.get("amount_vnd") != amount or action.get("payer") != "LOGIX" or action.get("basis") != "policy":
            return Verdict.modify("Tính lại quyền lợi từ tracking DB và chính sách", amount_vnd=amount,
                                  payer="LOGIX", basis="policy")

    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("Không đủ độ trễ hoặc nguyên nhân được ghi nhận để quy lỗi hãng")
        if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
            return Verdict.deny("Kiện hàng đã có bản ghi lỗi hãng")
        return Verdict.modify("Đối chiếu đúng kiện hàng, hãng và độ trễ từ DB",
                              parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                              driver_id=parcel.get("driver_id"), delay_days=delay)

    return Verdict.allow()
