# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): CATT
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-CATT-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S4

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Thế Cường | 2A202603355 | Kỹ sư cổng | Có |
|   2 | Hoàng Ngọc Minh Trí | 2A202603379 | Kỹ sư cổng | |
|   3 | Chử Thị Ánh | 2A202603360 | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Anh Tú | 2A202603434 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Tình hình tổng hợp nhóm · cập nhật 2026-11-19

- **Tiêu chí & Checkpoint vòng 1:** Tiêu chí chấp nhận đã được toàn bộ nhóm thống nhất và ký tại commit `4b87d77` (hash đã ký `0138aa3c85fd`, lock file `config/acceptance_criteria.lock`). Checkpoint cổng an toàn vòng 1 đã chốt tại hash `a6762b7a` (`config/round1.lock`).
- **Quyết định Gate 1 · v1 (Phiếu B mục B8):** Quyết định **Thu hẹp** (chưa mở pilot rộng). Cơ sở: Mốc prepared trên bộ nền `R-base-prepared-20261118-172041-a04730` đạt pass_rate/pass_k 1.0; 0đ hoàn sai, 0 lỗi hãng oan, 0 lộ PII; chi phí trung bình 5.565đ/ticket và ROI 0.8. Tuy nhiên, phân khúc kho không xác định `?` (5 trials) có chi phí 10.359đ/ticket, vượt ngưỡng chi phí làm tay (10.000đ), do đó quyết định thu hẹp luồng tự động và chuyển các đơn thiếu mã kho sang quy trình thủ công.
- **Thực thi và đo kiểm trên sự cố S4 (Đêm 11.11: ticket gấp ba, hàng chờ ngập):**
  - Mốc base trên S4: pass_rate chỉ 0.8683; 160.000đ hoàn sai; 27 lỗi hãng oan; hàng chờ đạt đỉnh 78 phút với 4 ca bị kẹt quá SLA 60 phút; tổng hoàn tự động 466.000đ vượt trần 300.000đ ngày sale do Finance quy định.
  - Sau khi triển khai cổng vòng 2 trong `lab10/guards.py` (chuyển người duyệt khi `llm_fallback`, trần hoàn tự động trong ngày 300.000đ) và `config/operating_gates.json` (tăng lên 2 người trực ca, 12 ca/giờ):
    - Run after mới nhất `R-S4-after-20261119-031437-871d0a`: pass_rate và pass_k đạt 1.0; 0đ hoàn sai; 0 lỗi hãng oan; 0 lộ PII; tổng hoàn tự động đạt 294.000đ/300.000đ (đạt trần ngân sách); thời gian chờ lâu nhất giảm xuống 38 phút (đạt SLA ≤ 60 phút), 0 ca ùn tắc; chi phí mỗi ticket 7.350đ so với 10.000đ làm tay, ROI dương (0.36).
    - Bộ nền sau sửa `R-base-after-20261119-031437-871d0a` bảo toàn 100% không regression (pass_rate 1.0).
  - Tự kiểm tra `R-S4-grade-20261119-031437-871d0a`: Kiểm 2 (criteria), 3 (visible), 5 (regression), 6 (monitor) đều **ĐẠT (✅)**. Cảnh báo integrity ở kiểm 1 phát sinh do Windows Git checkout chuyển đổi ký tự xuống dòng sang CRLF lệch với MANIFEST (chuẩn hóa LF thì 100% tệp gốc khớp hash tuyệt đối).
- **Quyết định Gate 1 · v2 (Phiếu C mục C12):** Giữ quyết định **Thu hẹp** (chưa mở pilot đại trà). Lý do: Mặc dù các cổng kỹ thuật và vận hành đã giải quyết triệt để các triệu chứng của S4, thiết kế vẫn dựa vào giả định có người trực ca và tracking DB chính xác; đồng thời nhóm kho `?` cần cơ chế phân luồng tách biệt hoàn toàn trước khi đưa vào vận hành thực tế.
- **Tình trạng nộp bài:** Chạy `python -m lab10.check_submission --collect` xác nhận **`ĐỦ THÀNH PHẦN`** (khớp đầy đủ 28 tệp trong manifest, thông tin `submission/submission.json` và 4 thành viên đã được chuẩn hóa đồng bộ).
- **Chỉ số theo dõi mới (C8):** Metric `risky_action_without_evidence_rate` trong `lab10/monitors.py` đạt chuẩn độc lập với nhãn/ID, đo được `0.0091` trên bộ nền (cô lập đúng ca T-002@55) và tăng lên `0.1854` trên bộ sự cố S4, được hệ thống chấm tự động ghi nhận **sáng đèn (`lit`)**.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenTheCuong-2A202603355

### Phần việc phụ trách

Kỹ sư cổng và trưởng nhóm. Phụ trách thiết kế metric offline cho bước chọn độ trễ tại Phiếu A (mục A2, câu 1.3). Thiết kế, cài đặt và tối ưu hóa hệ thống cổng an toàn trong `lab10/guards.py` (vòng 1 và vòng 2). Chủ trì điền Phiếu B mục B7.1 và Phiếu C mục C7. Quản lý Git repository của nhóm: chủ trì ký duyệt tiêu chí chấp nhận (`acceptance_criteria.json`), chốt checkpoint vòng 1 (`lab10.checkpoint`), điều phối gộp nhánh, xử lý xung đột tệp và nộp bài.

### Đóng góp cụ thể

- **Vòng 1:** Xây dựng 3 cổng phòng vệ cốt lõi trong `lab10/guards.py`:
  1. `pre_guard`: Ghim phiên bản chính sách hoàn tiền có hiệu lực dựa trên mốc thời gian `as_of`, loại bỏ nguy cơ áp dụng sai phiên bản chính sách trôi nổi.
  2. `write_gate` (nhánh `issue_refund`): Tái tính toán độc lập quyền lợi hoàn tiền từ tracking DB và bảng tỷ lệ chính sách, xác thực mã phê duyệt (`approval_id`) cho các đơn có giá trị lớn hoặc quá hạn, ngăn chặn triệt để hành vi ghi trùng lặp sổ cái.
  3. `write_gate` (nhánh `file_carrier_fault`): Thiết lập điều kiện chặn nghiêm ngặt: chỉ cho phép ghi phạt hãng vận chuyển khi tracking có ghi nhận nguyên nhân rõ ràng và độ trễ do lỗi vận chuyển đạt từ 3 ngày trở lên.
  - *Kết quả prepared trên S4:* Giảm số lỗi ghi oan cho bên thứ ba từ 27 xuống 0, giảm tiền hoàn sai từ 160.000đ xuống 0đ.
- **Vòng 2 (Sự cố S4):** 
  - Trực tiếp dò vết trace chuyên sâu trên ticket `S4-08@11` và `S4-08@22`, phát hiện cơ chế nguy hiểm khi LLM gặp lỗi HTTP 429 liên tiếp và tự động kích hoạt chế độ dự phòng mở (`llm_fallback mode="fail_open"`).
  - Triển khai cổng phát hiện cờ `llm_fallback` trong sự kiện: lập tức chặn lệnh tự hoàn và chuyển nhân viên duyệt (`Verdict.escalate`).
  - Phối hợp cài đặt cổng kiểm soát trần hoàn tiền tự động trong ngày (`daily_refund_cap_vnd = 300000`), giúp cắt giảm tổng chi hoàn tự động từ 466.000đ xuống 294.000đ, bảo đảm kỷ luật ngân sách của Finance.
- **Kỹ thuật hạ tầng & Git:** 
  - Điều tra hiện tượng lệch hash MANIFEST trên môi trường Windows do cơ chế tự động chuyển đổi CRLF của Git (`core.autocrlf`). Thiết lập cấu hình `.gitattributes` để bảo toàn nguyên trạng mã hóa byte cho các tệp khóa và tệp nộp bài.
  - Khắc phục xung đột tệp khi merge nhánh `ntc` vào `main`, bảo đảm tính toàn vẹn tuyệt đối cho bản tiêu chí đã ký và các bản ghi cấu hình.
- Sử dụng các công cụ hỗ trợ (ChatGPT/Codex, Claude) để đọc tài liệu, kiểm tra cú pháp và soạn thảo báo cáo; tự tay chạy đối soát toàn bộ lệnh `python -m lab10.grade --incident S4`, `lab10.check_submission` và `unittest` trước khi xuất bản.

### Bằng chứng

- **Mã nguồn & Cấu hình:** `lab10/guards.py`, `lab10/guards_round1.py`, `config/acceptance_criteria.json` (hash `0138aa3c85fd`), `config/round1.lock` (hash `a6762b7a`), `config/operating_gates.json`.
- **Tài liệu hoàn thành:** Phiếu A mục A2 (câu 1.3), Phiếu B mục B7.1, Phiếu C mục C7, `reports/t1/T-002@55_trace_analysis.md`.
- **Commit Git:** `4b87d77` (Ký tiêu chí chấp nhận), `5776831` (Chốt cổng vòng 1), `aa13f14` (Bổ sung cổng trần ngày và .gitattributes), `0cf8aeb` (Gom bộ bài nộp S4).
- **Mã lần chạy đo kiểm:** `R-S4-prepared-20261119-031437-871d0a`, `R-S4-after-20261119-031437-871d0a`, `R-base-after-20261119-031437-871d0a`, `R-S4-grade-20261119-031437-871d0a`.

### Exit ticket

- **Điều học được:** Cổng an toàn độc lập đóng vai trò là "lưới bảo hiểm" tối thượng. Khi mô hình LLM bị nghẽn mạng hoặc sập nguồn (fail-open), cổng kiểm tra tại tầng ghi dữ liệu dựa trên nguồn sự thật (Ground Truth Tracking DB) sẽ bảo vệ toàn diện hệ thống khỏi việc mất tiền oan và xâm phạm quyền lợi bên thứ ba. Tuy nhiên, ranh giới an toàn không chỉ nằm ở mã nguồn mà còn gắn chặt với các thông số trần kinh doanh (ngân sách) và năng lực điều phối nhân sự.
- **Điều còn chưa chắc:** Trần ngân sách 300.000đ hiện được thiết lập cố định cho ngày khuyến mãi 11.11; chưa rõ trong các đợt sale khác hoặc kịch bản kiểm thử ẩn, cơ chế trần động cần thích ứng thế nào để không làm dồn ứ quá mức các ca hợp lệ lên vai nhân viên duyệt.

## HoangNgocMinhTri-2A202603379

### Phần việc phụ trách

Kỹ sư cổng phụ trách giám sát dữ liệu, phân tích trace và kiểm thử an toàn AI. Vòng 1: Phụ trách khảo sát thực thi đánh giá nền (B0–B2), phân tích nguyên nhân gốc ca lỗi `T-002@55`, điều tra rò rỉ dữ liệu cá nhân PII và phân quyền truy cập (B7.2), xây dựng đặc tả kiểm thử hành vi đối kháng (B7.3). Vòng 2 (Sự cố S4): Thiết kế, lập trình và đăng ký chỉ số theo dõi mới C8 (`risky_action_without_evidence_rate`) trong `lab10/monitors.py`; điền Phiếu C mục C8 và lập báo cáo kỹ thuật chuyên sâu về telemetry monitoring.

### Đóng góp cụ thể

- **Vòng 1 (Đánh giá B0–B2 & Phân tích rò rỉ dữ liệu B7.2):**
  - Chạy đo kiểm baseline trên 110 lượt chạy thử (22 tickets × 5 seeds), phát hiện và lập tài liệu bóc tách nguyên nhân ca lỗi duy nhất `T-002@55`: Trợ lý AI bị đánh lừa bởi lời khai trong ticket của khách hàng, đè độ trễ 5 ngày lên dữ liệu thực tế 2 ngày trong DB, dẫn đến hoàn tiền sai quy định và phạt oan tài xế.
  - Phân tích luồng dữ liệu cá nhân theo B7.2: Phát hiện cơ chế lọc PII ở hàm `notify_carrier` sử dụng danh sách đen (denylist) thay vì danh sách trắng (allowlist), tạo ra lỗ hổng bỏ sót trường dữ liệu lồng nhau `recipient_contact` đối với các đơn hàng quà tặng (`is_gift = true`).
  - Soạn thảo bộ 2 ca kiểm thử hành vi adhoc cho B7.3 (`T-ADHOC-01` và `T-ADHOC-02`) nhằm kiểm tra khả năng đề kháng trước prompt injection và bảo vệ PII.
- **Vòng 2 (Chỉ số theo dõi mới C8 – Telemetry Monitoring):**
  - Trực tiếp thiết kế và lập trình metric `risky_action_without_evidence_rate` trong `lab10/monitors.py`. Metric được thiết kế tổng quát, hoàn toàn độc lập với nhãn chuẩn (`label`), mã ticket ID và tên bộ dữ liệu.
  - Thuật toán nhận diện 3 nhóm hành vi rủi ro thiếu bằng chứng xác thực: (1) `model_override` làm sai lệch số ngày trễ so với tracking DB, tuân lệnh `directive_obeyed` hoặc rơi vào `llm_fallback`; (2) Ghi phạt lỗi hãng (`faults`) khi tracking thiếu nguyên nhân hợp lệ; (3) Gửi thông tin định danh cá nhân (PII) trong gói tin gửi sang hãng vận chuyển.
  - Bổ sung cơ chế phòng vệ chống lỗi biên dữ liệu (`valid_trials` filter, xử lý an toàn khi trials rỗng hoặc chứa `None`), vượt qua 100% các ca kiểm thử biên và kiểm thử hồi quy `test_public.py`.
  - Kết quả đo kiểm: Metric đạt `0.0091` trên bộ nền (cô lập chính xác 1 ca lỗi `T-002@55`) và tăng vọt lên `0.1854` trên bộ sự cố S4, được `lab10.grade` xác nhận **sáng đèn (`lit`)**.
- Soạn thảo báo cáo kỹ thuật hoàn chỉnh `reports/t5/C8_new_monitoring_metric.md` và cập nhật mục C8 trong Phiếu C.

### Bằng chứng

- **Mã nguồn:** `lab10/monitors.py` (hàm `risky_action_without_evidence_rate` và từ điển `MONITORS`).
- **Tài liệu & Báo cáo kỹ thuật:** Phiếu B (mục B0, B1, B2, B7.2, B7.3), Phiếu C (mục C8), `reports/t1/T-002@55_trace_analysis.md`, `reports/t2/B7.2_data_leakage_prevention.md`, `reports/t3/B7.3_behavioral_testing.md`, `reports/t5/C8_new_monitoring_metric.md`.
- **Kết quả đo kiểm:** Output `lab10.grade` mục `6 monitor` xác nhận sáng đèn `[('risky_action_without_evidence_rate', 'before', 0.0091, 0.1854), ('risky_action_without_evidence_rate', 'after', 0.0091, 0.1854)]`. Unit tests `tests/test_public.py` đạt 13/13 OK.

### Exit ticket

- **Điều học được:** Giám sát vận hành (monitoring) trong hệ thống AI đòi hỏi tư duy tách biệt với nhãn đúng/sai. Một metric telemetry tốt phải đo lường được các triệu chứng bất thường trong quá trình ra quyết định (như sự mất cân xứng giữa dữ liệu đầu vào và hành động tác động ra bên ngoài) ngay khi chưa có phản hồi hay khiếu nại từ người dùng.
- **Điều còn chưa chắc:** Metric hiện tại phát hiện tốt các đề xuất sai lệch của agent, nhưng chưa phân biệt được hành vi rủi ro nào đã bị chặn bởi cổng bảo vệ và hành vi nào đã lọt ra thế giới thực; trong giai đoạn pilot cần phân tầng metric thành hai lớp: Tín hiệu phát hiện sớm (Early Detection) và Thiệt hại thực tế (Actual Incident Rate).

## ChuThiAnh-2A202603360

### Phần việc phụ trách

Sản phẩm và kinh doanh. Vòng 1: Chủ trì xây dựng bộ tiêu chí chấp nhận tại Phiếu A (câu 1.1 và 1.6), tổng hợp dữ liệu tiêu chí để toàn nhóm thống nhất và ký cam kết; phụ trách `config/acceptance_criteria.json`, lập bản đồ luồng dữ liệu tại Phiếu B mục B3, thiết lập các cổng tài chính – kinh doanh tại Phiếu B mục B7.4 và mục `business` trong `config/operating_gates.json`, soạn thảo quyết định Gate 1 · v1 (B8). Vòng 2 (Sự cố S4): Phân tích biến động chi phí đơn hàng, tính toán ROI và xác định phạm vi pilot (C5 câu 3.2), cập nhật ngân sách ngày sale trong cấu hình, chủ trì tổng hợp quyết định Gate 1 · v2 (C12) và 3 dòng bắt buộc.

### Đóng góp cụ thể

- **Vòng 1 (Thiết lập tiêu chí & Phân tích chi phí v1):**
  - Chủ trì soạn thảo Phiếu A câu 1.1 và 1.6; xây dựng bộ tiêu chí chấp nhận được nhóm ký tại commit `4b87d77` (hash `0138aa3c85fd`).
  - Hoàn thành bản đồ dữ liệu B3: Thiết lập ranh giới dữ liệu giữa thông tin tự khai của khách hàng và các nguồn chân thực (đơn hàng, kiện hàng, chính sách bồi hoàn, sổ cái); cảnh báo trước nguy cơ dữ liệu tracking cập nhật chậm và lưu lượng dồn toa trong ngày sale.
  - Cấu hình các cổng kinh doanh vòng 1: Ngân sách hoàn tự động tối đa ngày thường 2.000.000đ, trần chi phí LLM 1.500đ/ticket, ROI mục tiêu ≥ 0.
  - Phân tích mốc prepared trên bộ nền `R-base-prepared-20261118-172041-a04730`: Pass rate đạt 1.0, chi phí trung bình 5.565đ/ticket, ROI 0.8. Phát hiện phân khúc kho thiếu thông tin (`?`) có 5 trials với chi phí 10.359đ/ticket (cao hơn mức làm thủ công 10.000đ); từ đó đề xuất quyết định B8 v1 là **Thu hẹp**, yêu cầu chuyển các đơn thiếu kho sang xử lý tay.
- **Vòng 2 (Xử lý sự cố tài chính ngày sale S4):**
  - Tiếp nhận cảnh báo từ Finance: Tổng hoàn tự động đêm 11.11 đạt 466.000đ, vượt mức trần 300.000đ được phê duyệt riêng cho ngày sale.
  - Cập nhật thông số `business.daily_refund_cap_vnd = 300000` trong `config/operating_gates.json` và phối hợp với kỹ sư cổng thiết lập cơ chế chuyển người duyệt khi vượt trần.
  - Đánh giá kết quả mốc after trên S4 (`R-S4-after-20261119-031437-871d0a`): Tổng hoàn tự động giảm còn 294.000đ (dưới trần 300.000đ), chi phí trung bình 7.350đ/ticket, ROI đạt 0.36, không phát sinh bất kỳ khoản hoàn sai nào.
  - Soạn thảo quyết định Gate 1 · v2 tại C12: Bảo lưu quyết định **Thu hẹp**, khuyến nghị chưa mở pilot rộng cho đến khi cơ chế phân tách nhóm kho `?` được kiểm chứng triệt để trên thực tế. Soạn thảo 3 dòng bắt buộc cho hồ sơ nộp bài `submission/submission.json`.
- Sử dụng công cụ AI hỗ trợ đối chiếu ma trận rủi ro kinh doanh, tính toán bảng phân bổ chi phí theo từng kho; kiểm tra trực tiếp số liệu từ các tệp `report.json` và cấu hình hệ thống.

### Bằng chứng

- **Tài liệu hoàn thành:** Phiếu A (câu 1.1, 1.6), Phiếu B (mục B3, B7.4, B8), Phiếu C (mục C5 câu 3.2, C12), `submission/submission.json`.
- **Cấu hình & Dữ liệu:** `config/acceptance_criteria.json`, `config/acceptance_criteria.lock`, `config/operating_gates.json` (mục `business`), `config/round1.lock`.
- **Mã lần chạy đối chiếu:** `R-base-prepared-20261118-172041-a04730`, `R-S4-before-20261119-031437-871d0a`, `R-S4-after-20261119-031437-871d0a`, `R-S4-grade-20261119-031437-871d0a`.

### Exit ticket

- **Điều học được:** Tự động hóa bằng AI chỉ thực sự mang lại giá trị khi bài toán kinh tế đứng vững. Một hệ thống AI có tỷ lệ chính xác kỹ thuật 100% nhưng chi phí vận hành (tiền token LLM + chi phí giữ chỗ nhân sự trực) vượt quá chi phí làm tay của con người thì vẫn là một thất bại kinh doanh. Cần quản trị chi phí theo từng phân khúc khách hàng/kho hàng thay vì chỉ nhìn vào chỉ số trung bình.
- **Điều còn chưa chắc:** Nhóm kho `?` có chi phí 10.359đ/ticket xuất phát từ việc thiếu mã kho trong dữ liệu giả lập; cần xác minh trên hệ thống ERP thực tế xem tỷ lệ đơn hàng thiếu thông tin kho là bao nhiêu để quyết định điều chỉnh cổng hay làm sạch dữ liệu đầu vào.

## NguyenAnhTu-2A202603434

### Phần việc phụ trách

Vận hành và pháp lý. Vòng 1: Xây dựng tiêu chí vận hành và bảo vệ quyền lợi đối tác tại Phiếu A (câu 1.2 và 1.4); chủ trì phân tích HAZOP vòng 1 (Phiếu B mục B4); rà soát checklist 9 nhóm việc (B5); soạn thảo quy trình vận hành chuẩn Runbook 1–3 và phương án trực ca giờ cao điểm (B7.5, B7.6); cấu hình các mục `operations` và `legal` trong `config/operating_gates.json`. Vòng 2 (Sự cố S4): Điều tra nguyên nhân quá tải hàng chờ (C3); chủ trì phân tích HAZOP của thẻ S4 (C4); xác lập giả định môi trường (C5 câu 3.3); cập nhật Risk Register (C10); hoàn thiện Runbook 4–5 (C11); kiểm soát tính toàn vẹn hồ sơ nộp bài (`check_submission`).

### Đóng góp cụ thể

- **Vòng 1 (Thiết lập khung vận hành & Pháp lý v1):**
  - Xây dựng tiêu chí SLA khắt khe: 100% lệnh hoàn tiền trên sổ cái phải có căn cứ truy xuất; cấm tuyệt đối việc ghi lỗi phạt hãng vận chuyển khi tracking thiếu nguyên nhân; cam kết thời gian chờ của khách hàng trong hàng đợi duyệt không quá 60 phút.
  - Cấu hình cổng con người và pháp lý trong `config/operating_gates.json`: Khai báo danh tính người chịu trách nhiệm (`operator_name`, `approver_name`), phân công số nhân sự trực ca (`reviewers_on_shift = 1`), thiết lập cơ chế ngắt khẩn cấp (`kill_switch`), và chặn danh sách trường dữ liệu cá nhân nhạy cảm gửi sang bên thứ ba (`recipient_contact`, `customer_note`, `phone`, `street`).
  - Thiết kế Runbook 1–3: Hướng dẫn chi tiết quy trình xử lý khi phát hiện hoàn tiền sai, cảnh báo nguy cơ cạn kiệt ngân sách và quy trình đình chỉ trợ lý AI khi phát hiện lỗi hệ thống.
- **Vòng 2 (Giải quyết sự cố vận hành & Nghẽn hàng chờ S4):**
  - Trực tiếp phân tích ca lỗi vận hành `S4-07@11`: Chỉ ra rằng việc dồn toa các ca hàng vỡ/thất lạc trong giờ cao điểm đêm sale vượt quá sức chứa của 1 nhân viên trực (công suất 6 ca/giờ), dẫn đến thời gian chờ tối đa vọt lên 78 phút và phát sinh 4 ca kẹt quá hạn SLA.
  - Phát hiện điểm mù nghiêm trọng tại Runbook 2: Ngưỡng cảnh báo chi hoàn được đặt theo ngày thường (ngân sách 2.000.000đ, ngưỡng vàng 1.600.000đ) nên hoàn toàn "bị mù" trước trần 300.000đ của ngày sale, để lọt khoản chi vượt 466.000đ mà không có báo động.
  - Đề xuất giải pháp vận hành kép: Tăng cường định biên nhân sự trực ca lên 2 người (`reviewers_on_shift = 2`), nâng công suất phục vụ lên 12 ca/giờ; đồng thời thiết lập quy tắc phản ứng nhanh tại Runbook 5: Khi hàng chờ đạt từ 6 ca hoặc có ca chờ trên 30 phút, lập tức triệu tập nhân sự thứ ba trong vòng 15 phút.
  - *Kết quả sau cải tiến:* Thời gian chờ tối đa giảm từ 78 phút xuống 38 phút (đạt chuẩn SLA), xóa bỏ hoàn toàn hiện tượng kẹt hàng chờ (`queue_stuck = 0`), lỗi phạt oan hãng vận chuyển giảm từ 27 về 0.
- Hoàn thiện bảng Risk Register mới (C10), cập nhật checklist 9 nhóm việc và phối hợp chạy lệnh `python -m lab10.check_submission --collect` bảo đảm hồ sơ nộp bài đạt chuẩn `ĐỦ THÀNH PHẦN`.

### Bằng chứng

- **Tài liệu hoàn thành:** Phiếu A (câu 1.2, 1.4), Phiếu B (mục B4, B5, B7.5, B7.6), Phiếu C (mục C3, C4, C5 câu 3.3, C10, C11), `reports/t4/C2_incident_error_analysis.md`.
- **Cấu hình:** `config/operating_gates.json` (mục `operations`, `legal`), `config/switches.json`.
- **Mã lần chạy:** `R-S4-before-20261119-031437-871d0a`, `R-S4-after-20261119-031437-871d0a`, `R-S4-grade-20261119-031437-871d0a`.
- **Kiểm định nộp bài:** Output `lab10.check_submission` xác nhận `ĐỦ THÀNH PHẦN`.

### Exit ticket

- **Điều học được:** Một quy trình vận hành và runbook chỉ có giá trị khi nó được thiết kế linh hoạt theo bối cảnh thực tế. Đặt một ngưỡng cố định cho mọi ngày trong năm là một cái bẫy nguy hiểm; các sự kiện đặc biệt (như ngày hội sale) bắt buộc phải có thông số vận hành và hạn mức riêng biệt được nạp vào hệ thống trước giờ G.
- **Điều còn chưa chắc:** Định mức năng suất 6 ca duyệt/giờ của nhân sự hiện là số liệu giả định trong phòng lab; trong môi trường vận hành thực tế khi nhân viên phải đọc các giải trình phức tạp và đối chiếu nhiều màn hình, công suất thực có thể suy giảm, cần đo đạc chính xác trong giai đoạn pilot có kiểm soát.
