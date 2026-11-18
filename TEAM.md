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

## Tình hình tổng hợp nhóm · cập nhật 2026-11-18

- Tiêu chí đã ký ở commit `4b87d77`; checkpoint cổng vòng 1 là `a6762b7a`. Quyết định B8 v1: **Thu hẹp**, do nhóm kho `?` có chi phí 10.359đ/ticket, cao hơn làm tay 10.000đ.
- Trên S4 after `R-S4-after-20261118-203211-8b4b71`: pass_rate/pass_k 1.0; hoàn sai, lỗi hãng oan và PII đều 0; hoàn tự động 294.000/300.000đ; chờ lâu nhất 41 phút, 0 ca ùn; chi phí 7.740đ/ticket, ROI 0.29. Grade `R-S4-grade-20261118-203206-8b4b71` vẫn **FAIL integrity**; chưa có hidden tests.
- Quyết định C12 v2 là **Thu hẹp**, nhưng `pilot_scope` hiện vẫn `all`; chưa chứng minh ticket kho `?` đã được chuyển khỏi luồng tự động. Chưa mở pilot cho tới khi nhóm xác minh cách thực thi và Lab Coach/nhóm xử lý lỗi integrity. PIC chưa ký B8/C12.
- `python -m lab10.check_submission` còn thiếu B6, C0, C1, C2, C6, C7, C9; manifest trong `submission/` cần tạo lại sau khi hoàn tất chỉnh sửa `submission.json`. Danh sách thành viên trong submission hiện mới có Ánh; cần Cường phối hợp thu đủ thông tin.
- C8 monitor trong report là `0.1854` trên S4 so với `0.0091` bộ nền; Trí cần hoàn tất cách diễn giải vì chỉ số hiện cũng tính tín hiệu `llm_fallback`, không chỉ hành động gây hại.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenTheCuong-2A202603355

### Phần việc phụ trách

Kỹ sư cổng và trưởng nhóm. Câu 1.3 (metric offline cho bước chọn độ trễ, Phiếu A mục A2). Viết `lab10/guards.py` vòng 1 và điền Phiếu B mục B7.1; vòng 2 dò trace `S4-08` và sửa cổng cho thẻ S4, phần code ở Phiếu C mục C7. Quản lý Git của bàn: ký tiêu chí sau khi nhóm duyệt, chốt cổng vòng 1, gộp nhánh và push bài.

### Đóng góp cụ thể

- Vòng 1: viết ba cổng trong `lab10/guards.py`: `pre_guard` ghim chính sách có hiệu lực theo `as_of`; `write_gate` nhánh `issue_refund` tính lại quyền lợi từ tracking DB và chính sách, kiểm phê duyệt, chặn ghi lặp; nhánh `file_carrier_fault` chỉ cho ghi lỗi hãng khi tracking có nguyên nhân và đủ độ trễ. Ở mốc prepared trên thẻ S4, lỗi ghi oan cho hãng giảm từ 27 xuống 0, hoàn sai từ 160.000đ xuống 0.
- Vòng 2: dò `S4-08@11` (LLM trả 429, rơi về `fail_open`, cổng vẫn chặn ghi lỗi hãng VNX vì nguyên nhân thật là `MERCHANT_HANDOVER`) và `S4-08@22` (đạt). Thêm cổng trần hoàn tự động trong ngày; nhóm giữ bản của Tú khi gộp vì cho cùng kết quả (tổng hoàn tự động 466.000đ ở base, còn 292.000đ ≤ 300.000đ ở after).
- Tìm và sửa lỗi xuống dòng: Git trên Windows (`core.autocrlf=true`) làm hash file khoá lệch MANIFEST, và hash tiêu chí đã ký là của bản CRLF. Thêm `.gitattributes` để tiêu chí và bản chốt vòng 1 giữ đúng hash trên mọi máy, kể cả máy của team chấm.
- Gộp nhánh: phát hiện nhánh `ntc` mang thay đổi xoá trắng tiêu chí đã ký, `operating_gates.json` và Phiếu A khi merge; trả lại đúng bản `main` trước khi commit.

Sử dụng ChatGPT/Codex và Claude để đọc mã nguồn, chẩn đoán lỗi hash và xung đột merge, soạn nháp nội dung phiếu và mục này. Tôi đọc lại, chạy lại `python -m lab10.grade --incident S4` và `python -m unittest` trên máy mình trước khi push.

### Bằng chứng

- `lab10/guards.py`, `lab10/guards_round1.py`; Phiếu A mục A2 (câu 1.3); Phiếu B mục B7.1; Phiếu C mục C7.
- Commit: `5776831` (chốt vòng 1 và bằng chứng Gate 1), `aa13f14` (cổng trần ngày, `.gitattributes`), `7336d9e` (gộp `main` vào `ntc`).
- Lần chạy: `R-S4-prepared-20261118-212644-2d0a9f`, `R-S4-after-20261118-212644-2d0a9f`, `R-base-after-20261118-212643-2d0a9f`; trace `S4-08@11`, `S4-08@22`.

### Exit ticket

*(Bản nháp, Cường đọc và sửa theo ý mình trước khi nộp.)*

Điều học được: cổng kiểm lệnh ghi so với nguồn sự thật (tracking DB) thì không phụ thuộc LLM đúng hay lỗi, nên S4-08 vẫn an toàn khi LLM rơi về `fail_open`; nhưng cổng kỹ thuật không giải quyết được ngân sách và người trực, phải có con số trong config và người chịu trách nhiệm. Ngoài ra, một khác biệt xuống dòng LF/CRLF cũng đủ làm hỏng "ký trước khi đo", nên tính toàn vẹn phải được kiểm trên đúng máy của người chấm.

Điều còn chưa chắc: trần 300.000đ chỉ đúng cho ngày 11.11 trong dữ liệu giả lập; chưa biết bài kiểm tra ẩn có ngày với ngân sách khác không, và cổng "LLM lỗi thì chuyển người" có làm hàng chờ ùn khi LLM lỗi kéo dài hơn trong pilot thật hay không.

## ChuThiAnh-2A202603360

### Phần việc phụ trách

Sản phẩm và kinh doanh. Vòng 1: chủ trì Phiếu A câu 1.1 và 1.6, tổng hợp tiêu chí để nhóm duyệt; phụ trách `config/acceptance_criteria.json`, Phiếu B mục B3 và B7.4, mục `business` trong `config/operating_gates.json`, quyết định B8 v1. Vòng 2 thẻ S4: đọc chi phí, ROI và phạm vi pilot; phụ trách C5 câu 3.2, cập nhật mục `business`, tổng hợp C12 v2 và ba dòng bắt buộc.

### Đóng góp cụ thể

Đã chủ trì Phiếu A câu 1.1 và 1.6; tiêu chí đã được nhóm duyệt và ký tại commit `4b87d77` (hash `0138aa3c`). Đã hoàn thành bản đồ dữ liệu B3: phân biệt lời khai trong ticket với nguồn về đơn, kiện hàng, chính sách, phê duyệt và sổ hoàn; ghi nhận rủi ro tracking cập nhật trễ, nhập tay sai và ticket dồn giờ sale. Đã điền B7.4 và các cổng business vòng 1 theo dữ liệu lab: ngân sách hoàn ngày 2.000.000đ, trần LLM 1.500đ/ticket, phạm vi toàn bộ và ROI tối thiểu 0.

Đã chạy checkpoint vòng 1 (hash `a6762b7a`) và kiểm tra run prepared `R-base-prepared-20261118-172041-a04730`: pass_rate/pass_k đều 1.0; hoàn sai, lỗi hãng oan, lộ PII và queue_stuck đều 0; chi phí 5.565đ/ticket, ROI 0.8. Phân khúc kho `?` có 5 trials và chi phí 10.359đ/ticket, cao hơn chi phí làm tay; B8 v1 chọn Thu hẹp, yêu cầu chuyển ticket không xác định kho sang làm tay.

Ở vòng 2 đã điền C5 câu 3.2 và đặt trần hoàn ngày sale 300.000đ trong `config/operating_gates.json`. Đã chốt yêu cầu khi `policy_check` rơi vào `fail_open`: chuyển người duyệt, không tự hoàn, ghi lỗi hoặc gửi thông báo lỗi hãng; thay đổi code tương ứng cần kỹ sư cổng rà soát. S4 after `R-S4-after-20261118-203211-8b4b71`: pass_rate/pass_k 1.0, hoàn sai/lỗi hãng oan/PII đều 0, tổng hoàn tự động 294.000đ/300.000đ, chờ lâu nhất 41 phút, 0 ca ùn, chi phí 7.740đ/ticket, ROI 0.29. Bộ nền after `R-base-after-20261118-203149-8b4b71` không có ca mới hỏng; `python -m unittest discover -s tests` chạy 13 tests, đều đạt.

Đã điền C12 và ba dòng bắt buộc; đề xuất Thu hẹp, chưa mở pilot. Grade `R-S4-grade-20261118-203206-8b4b71` vẫn FAIL ở `integrity`: nhiều file khóa không khớp `lab10/MANIFEST.json`; visible, regression và monitor đạt, hidden tests không có trên máy. `pilot_scope` vẫn là `all`, nên chưa có bằng chứng cấu hình đã chuyển nhóm kho `?` sang làm tay. Cần PIC xác nhận quyết định và nhóm/Lab Coach xử lý các điểm này trước khi mở pilot.

Dùng AI hỗ trợ rà soát hướng dẫn, đối chiếu số liệu và soạn bản nháp; các giá trị cấu hình và kết quả chạy được kiểm tra lại với file cấu hình và report trong repo.

### Bằng chứng

`templates/form-a-criteria.md` (câu 1.1, 1.6); `config/acceptance_criteria.json` (hash `0138aa3c`); `templates/form-b-evaluation-gates.md` (B3, B7.4, B8); `templates/form-c-incident.md` (C5.3.2, C12); `config/operating_gates.json`; `config/round1.lock` (hash `a6762b7a`); `submission/submission.json`; `runs/R-base-before-20261118-162921-7b0ef9/report.json`; `runs/R-base-prepared-20261118-172041-a04730/report.json`; `runs/R-base-after-20261118-203149-8b4b71/report.json`; `runs/R-S4-grade-20261118-203206-8b4b71.json`.

### Exit ticket

Điều học được: cổng vòng 1 có thể đưa các lỗi hoàn tiền và ghi lỗi hãng về 0 trong bộ prepared, nhưng chi phí trung bình và ROI vẫn thay đổi; cần đọc cả phân khúc thay vì chỉ nhìn số tổng.

Điều còn chưa chắc: nhóm `?` có 5 trials và chi phí 10.359đ/ticket nhưng chưa xác định được nguồn của nhãn kho; cần kiểm tra và quyết định chuyển nhóm này sang làm tay hay xử lý bằng phạm vi pilot trước khi kết luận.

## NguyenAnhTu-2A202603434

### Phần việc phụ trách

Vận hành và pháp lý. Vòng 1: câu 1.2 và 1.4 (Phiếu A), HAZOP vòng 1 và checklist 9 nhóm việc (Phiếu B mục B4, B5), Runbook 1–3 và giờ cao điểm (B7.5, B7.6), mục `operations` và `legal` trong `config/operating_gates.json`. Vòng 2 (thẻ S4): C3 phần giờ cao điểm, HAZOP của thẻ (C4), giả định môi trường (C5 câu 3.3), risk register (C10), Runbook 4–5 (C11), `submission/submission.json` và gom bài.

### Đóng góp cụ thể

Viết các tiêu chí vận hành và pháp lý (sổ cái khớp căn cứ, hãng chỉ bị ghi lỗi khi tracking có nguyên nhân, người duyệt xử lý trong hạn 60 phút) và thước đo cho bước ghi lỗi hãng. Điền cổng vận hành: người đứng tên, người duyệt, số người trực, điều kiện dừng, trường dữ liệu cá nhân không gửi hãng. Ở thẻ S4 chỉ ra ba điểm hỏng đo được ở mốc base: LLM trả 429 làm trợ lý rơi về `fail_open` và ghi lỗi oan cho hãng (`S4-08@11`), tổng hoàn tự động 466.000đ vượt ngân sách ngày 11.11 là 300.000đ, và hàng chờ có ca chờ 78 phút với một người trực. Phát hiện ngưỡng tiền ở Runbook 2 đặt theo ngân sách ngày thường 2.000.000đ nên không báo được sự cố này.

Sử dụng Claude để đọc mã nguồn và đề, soạn bản nháp các phiếu và script điền phiếu. Tôi đọc lại nội dung, chạy script trên máy mình, chạy kiểm tra JSON và `python3 -m unittest`, rồi tự commit và push. Các con số ngưỡng trong runbook là đề xuất của nhóm, chưa phải số đã đo ở pilot thật.

### Bằng chứng

`templates/form-a-criteria.md` (câu 1.2, 1.4); `templates/form-b-evaluation-gates.md` (B4, B5, B7.5, B7.6); `templates/form-c-incident.md` (C4, C5 câu 3.3, C10, C11); `config/operating_gates.json` (mục `operations`, `legal`). Mã commit và mã lần chạy base, prepared, after của thẻ S4 sẽ bổ sung sau khi chạy.

### Exit ticket

Điều học được: một ngưỡng vận hành chỉ đúng với hoàn cảnh nó được đặt; ngưỡng tiền 2.000.000đ cho ngày thường không báo được ngày sale có ngân sách 300.000đ, nên runbook phải có ngưỡng riêng cho ngày đặc biệt. Điều còn chưa chắc: con số 6 ca/giờ cho một người duyệt và khoảng 11 ca chuyển người mỗi giờ cao điểm đều lấy từ dữ liệu giả lập, cần đo lại ở pilot thật.
