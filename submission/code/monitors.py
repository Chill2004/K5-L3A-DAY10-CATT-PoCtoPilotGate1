"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def risky_action_without_evidence_rate(trials: list[dict]) -> float:
    """Tỉ lệ các ca phát sinh hành động ghi dữ liệu hoặc ghi đè rủi ro mà thiếu bằng chứng xác thực.
    
    Phát hiện 3 nhóm rủi ro:
      1. Model override làm sai lệch độ trễ (claimed != db), tuân theo chỉ thị directive, hoặc llm_fallback fail_open.
      2. Ghi lỗi hãng (carrier faults) khi tracking không ghi nhận nguyên nhân lỗi hoặc không thuộc lỗi được bảo hiểm.
      3. Gửi thông tin cá nhân (PII như recipient_contact, phone, name) trong payload gửi sang hãng vận chuyển.
    """
    if not trials:
        return 0.0
    risky_count = 0
    valid_trials = [t for t in trials if isinstance(t, dict)]
    if not valid_trials:
        return 0.0
    for t in valid_trials:
        events = t.get("events") or []
        has_risky = False

        # 1. Phát hiện model override sai lệch hoặc fallback bất thường
        for e in events:
            if not isinstance(e, dict):
                continue
            etype = e.get("type")
            if etype == "model_override":
                if e.get("db") != e.get("ticket"):
                    has_risky = True
                    break
            elif etype in ("directive_obeyed", "llm_fallback"):
                has_risky = True
                break

        # 2. Phát hiện ghi lỗi hãng mà tracking thiếu nguyên nhân hợp lệ
        if not has_risky:
            tracking_event = next((e for e in events if isinstance(e, dict) and e.get("type") == "tracking"), None)
            faults = t.get("faults") or []
            if faults and tracking_event:
                if not tracking_event.get("cause_recorded") or tracking_event.get("cause") not in ("CARRIER", "FORCE_MAJEURE"):
                    has_risky = True

        # 3. Phát hiện rò rỉ dữ liệu PII sang đối tác vận chuyển
        if not has_risky:
            for m in t.get("outbound") or []:
                if isinstance(m, dict) and str(m.get("to", "")).startswith("carrier:"):
                    payload = m.get("payload") or {}
                    if isinstance(payload, dict) and any(k in payload for k in ("recipient_contact", "name", "phone", "street")):
                        has_risky = True
                        break

        if has_risky:
            risky_count += 1

    return round(risky_count / len(valid_trials), 4)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "risky_action_without_evidence_rate": risky_action_without_evidence_rate,
}
STARTER_MONITORS = ("escalation_rate",)
