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
|   1 | Cường (bổ sung họ tên đầy đủ) | 2A202603355 | Kỹ sư cổng | Có |
|   2 | Trí (bổ sung họ tên đầy đủ) | Cần bổ sung | Kỹ sư cổng | |
<<<<<<< HEAD
|   3 | Chử Thị Ánh | 2A202603360 | Sản phẩm và kinh doanh | |
|   4 | Tú (bổ sung họ tên đầy đủ) | Cần bổ sung | Vận hành và pháp lý | |
=======
|   3 | Ánh (bổ sung họ tên đầy đủ) | Cần bổ sung | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Anh Tú | 2A202603434 | Vận hành và pháp lý | |
>>>>>>> main

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## Cuong-2A202603355

Cần thay `Cuong` trong tiêu đề bằng họ tên đầy đủ không dấu trước khi nộp.

### Phần việc phụ trách

Kỹ sư cổng và trưởng nhóm. Phụ trách câu 1.3, thiết kế metric offline cho bước chọn độ trễ tại Phiếu A mục A2. Viết và sửa `lab10/guards.py`, điền Phiếu B mục B7.1 và phần sửa code tại Phiếu C mục C7. Quản lý Git, thực hiện ký tiêu chí sau khi nhóm duyệt, chốt cổng vòng 1 và push bài.

### Đóng góp cụ thể

Đã bổ sung thiết kế metric chọn độ trễ tại A2, gồm thước đo, dữ liệu và người tạo nhãn chuẩn, công thức tính, xử lý ca thiếu dữ liệu và điểm mù. Các phần code, ký tiêu chí và chốt vòng 1 sẽ cập nhật theo tiến độ thực tế.

Sử dụng ChatGPT/Codex để đọc hướng dẫn, hỗ trợ phân công và soạn nội dung metric câu 1.3 cùng mục cá nhân này.

### Bằng chứng

`templates/form-a-criteria.md`, mục A2, cột Offline câu 1.3. Mã commit và mã lần chạy sẽ bổ sung sau khi thực hiện.

### Exit ticket

Cường tự bổ sung một điều học được và một điều còn chưa chắc trước khi nộp.

## ChuThiAnh-2A202603360

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

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
