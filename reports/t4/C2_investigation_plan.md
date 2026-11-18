# Kế hoạch Điều tra Sự cố & Đặc tả Sẵn sàng (C2)

**Dự án:** LogiX-VN AI Refund Assistant (PoC đến Pilot Gate 1)  
**Nhiệm vụ:** T4 – C2 Phân tích Lỗi Sự cố  
**Vai trò:** Điều tra viên Sự cố An toàn AI cao cấp & Kỹ sư Phân tích Nguyên nhân Gốc rễ (RCA)  
**Ngày:** 2026-11-18  
**Trạng thái Hiện tại:** **BỊ CHẶN – ĐANG CHỜ SỰ CỐ**  

---

## 1. Tóm tắt Điều hành & Kiểm toán Tính sẵn có Sự cố

Theo quy tắc thực thi Lab 10, các gói sự cố (`incidents/S1/` đến `incidents/S8/`) được Lab Coach phát hành tại Phút 125 của buổi học thông qua git dispatch upstream.

### 1.1 Trạng thái Repository
- **Thư mục Mục tiêu:** `incidents/`
- **Nội dung Thư mục Hiện tại:** Chỉ chứa `incidents/README.md` (không có thư mục con sự cố hoặc thẻ nào).
- **Cấu hình Remote:**
  - `origin`: `https://github.com/Chill2004/K5-L3A-DAY10-CATT-PoCtoPilotGate1.git`
  - `upstream`: Hiện chưa được cấu hình trong git remotes.
- **Thực thi Probe:**
  Chạy `python -m lab10.grade --incident S1` xác nhận:
  ```text
  TỪ CHỐI KIỂM TRA: chưa có gói sự cố S1 trên máy này (thiếu incidents/S1/tickets.jsonl, incidents/S1/world_patch.json).
  Thẻ sự cố chỉ được phát ở phút 125 của buổi học.
  ```
- **Kết luận:** Chưa có gói sự cố nào được phát hành. Để duy trì tính toàn vẹn học thuật và kỹ thuật, **không có sự cố, mã ticket, trace thất bại, hoặc nguyên nhân gốc nào được bịa đặt**. Nhiệm vụ C2 được đánh dấu là **BỊ CHẶN – ĐANG CHỜ SỰ CỐ**.

---

## 2. Quy trình Tiếp nhận & Thiết lập Sự cố

Khi Lab Coach công bố phát hành thẻ sự cố, điều tra viên phải thực hiện giao thức sau:

### Bước 1: Cấu hình Upstream Remote (nếu chưa có)
```bash
git remote add upstream https://github.com/VinUni-AI20k/K5_L3_Day10_PoC-to-Pilot_Gate1_student.git
git remote -v
```

### Bước 2: Tiếp nhận Gói Sự cố
```bash
git pull --no-rebase --no-edit --allow-unrelated-histories -X ours upstream main
```
*Các Artifact Mong đợi:*
- Thư mục `incidents/Sx/` (trong đó `Sx` $\in \{S1, \dots, S8\}$ là thẻ sự cố được rút).
- File gốc `incident-cards.md`.
- Các file fixture: `incidents/Sx/tickets.jsonl`, `incidents/Sx/world_patch.json`, `incidents/Sx/card.json`, và `incidents/Sx/card.md`.

### Bước 3: Ghi nhận Phân công Sự cố trong Form C
Cập nhật `templates/form-c-incident.md`:
- Ghi mã thẻ đã rút vào `Thẻ đã bốc: Sx`.
- Thực thi kiểm tra baseline ban đầu trên hệ thống chưa sửa đổi:
  ```bash
  python -m lab10.grade --incident Sx
  ```

---

## 3. Phương pháp Điều tra & Khung RCA

Khi fixture sự cố có sẵn, quy trình phân tích sau sẽ được áp dụng để điều tra ít nhất hai thất bại khác biệt.

### 3.1 Tiêu chí Lựa chọn Ticket Thất bại
Từ báo cáo đánh giá sự cố (`runs/<run_id>/report.json`), các ticket thất bại sẽ được lọc:
1. **Quy tắc Lựa chọn Ticket:** Chọn ít nhất hai ticket thất bại ($T_1, T_2$) thể hiện các mẫu thất bại khác biệt hoặc các danh mục nguồn gốc khác biệt.
2. **Quy tắc Lựa chọn Seed:** Xác định các seed thể hiện thất bại xác định vs. ngẫu nhiên (ví dụ seed 11 vs. seed 55).
3. **Yêu cầu Lỗi Ẩn:** Ít nhất một ticket được chọn phải thể hiện **Lỗi Ẩn (Lỗi chìm)**, nơi agent dường như thành công hoặc tuyên bố một hành động, nhưng trạng thái bên dưới (sổ cái, lỗi hãng, hoặc payload gửi đi) chịu vi phạm an toàn im lặng.

### 3.2 Quy trình Tái tạo Trace
Đối với mỗi ticket được chọn, thực thi lệnh trace:
```bash
python -m lab10.trace --suite Sx --ticket <TICKET_ID> --seed <SEED>
```
Trace sẽ được phân tích theo taxonomy sự kiện chuẩn hóa:

| Loại Sự kiện Trace | Thành phần được Kiểm tra | Câu hỏi Điều tra Quan trọng |
|---|---|---|
| `llm_extract` | `MockLLM.extract` | Model có ảo giác, tuân theo directive prompt injection, hoặc bịa đặt sự kiện không? |
| `tracking` | `ReadTools.lookup_order` | Tracking sự thật gốc có được lấy chính xác không? `db_delay_days` là bao nhiêu? |
| `model_override` | `agent.py:127-130` | Agent có ghi đè sự thật cơ sở dữ liệu bằng claim văn bản không đáng tin không? |
| `policy` | `H.effective_policy` | Agent có đánh giá đúng phiên bản policy đang hoạt động không? |
| `proposal` | Business Engine | Quyền lợi hoàn tiền đề xuất có được tính toán đúng không? |
| `approval_used` | `ReadTools.lookup_approvals` | Phê duyệt có hợp lệ, chưa hết hạn, và áp dụng đúng order/customer không? |
| `tool: issue_refund` | `WriteTools.issue_refund` | Có ghi sổ cái tài chính trái phép xảy ra không? Payer là ai? |
| `tool: file_carrier_fault` | `WriteTools.file_carrier_fault` | Có strike không chính đáng được ghi chống hãng logistics không? |
| `tool: notify_carrier` | `WriteTools.notify_carrier` | Payload có rò rỉ PII khách hàng bị hạn chế không? |
| `tool: send_reply` | `WriteTools.send_reply` | Phản hồi khách có mâu thuẫn với trạng thái sổ cái nội bộ không? |
| `gate` / `legal_gate` | `guards.py` / `tools.py` | Guard hệ thống có chặn hoặc thất bại trong việc bắt độ lệch không? |

### 3.3 Các Chiều Phân loại Nguyên nhân Gốc & Thất bại
Mọi thất bại sẽ được phân loại theo hai chiều trực giao:

#### Chiều A: Phân loại Thất bại
1. **Giới hạn hệ thống (System Limitation):** Thất bại ranh giới kiến trúc hoặc thành phần vốn có.
2. **Lỗi ngữ cảnh (Context Error):** Agent bị dẫn dắt sai bởi ngữ cảnh mâu thuẫn, thiếu, hoặc mơ hồ.
3. **Lỗi chìm (Hidden Error):** Thất bại im lặng nơi cả khách hàng lẫn agent đều không nhận ra khiếm khuyết; rò rỉ tài chính hoặc thiệt hại bên thứ ba xảy ra mà không có lỗi bên ngoài.

#### Chiều B: Danh mục Nguồn Gốc
1. `Ticket text` (ví dụ Prompt injection, claim phóng đại, directive chưa xác minh).
2. `Tracking database` (ví dụ Thiếu scan, timestamp xung đột, thiếu nguyên nhân chậm).
3. `Policy index` (ví dụ Cache policy cũ, cờ index không hoạt động, cửa sổ ngày không khớp).
4. `Approval table` (ví dụ Phê duyệt hết hạn, tái sử dụng ID phê duyệt, mismatch customer ID).
5. `LLM fallback` (ví dụ Fallback rate limit 429 dẫn đến giải ngân tài chính mở).
6. `Human queue` (ví dụ Backlog SLA, queue starvation, escalation không xử lý).
7. `Operating configuration` (ví dụ Thiếu trần hoàn tiền hàng ngày, denylist PII pháp lý chưa cấu hình).

---

## 4. Kiểm kê Sự cố Pre-Configured & Template So sánh

```markdown
### C2.1 Kiểm kê Sự cố
| Sự cố | Mã Ticket | Seed Có sẵn | Mô tả Thất bại | Danh mục Nguồn Gốc | Danh mục Thất bại | Trạng thái Điều tra |
|---|---|---|---|---|---|---|
| Sx | [TBD] | [TBD] | [Đang chờ phát hành sự cố] | [TBD] | [TBD] | BỊ CHẶN |
| Sx | [TBD] | [TBD] | [Đang chờ phát hành sự cố] | [TBD] | [TBD] | BỊ CHẶN |

### C2.5 Ma trận So sánh Cross-Failure
| Chiều | Thất bại 1 | Thất bại 2 |
|---|---|---|
| Mã Ticket | [TBD] | [TBD] |
| Seed | [TBD] | [TBD] |
| Danh mục Thất bại | [TBD] | [TBD] |
| Nguồn Gốc Chính | [Nguồn A] | [Nguồn B (Phải khác A)] |
| Điểm Phân kỳ Đầu tiên | [Bước & Sự kiện] | [Bước & Sự kiện] |
| Lỗi Ẩn được Xác nhận | [Có / Không với Bằng chứng] | [Có / Không với Bằng chứng] |
| Tác động Sổ cái (VND) | [Số tiền Ghi Thực tế] | [Số tiền Ghi Thực tế] |
| Tác động An toàn & Pháp lý | [Thiệt hại Tài chính/Đối tác/PII] | [Thiệt hại Tài chính/Đối tác/PII] |
```

---

## 5. Các Chặn Hiện tại & Các Bước Tiếp theo Ngay lập tức

1. **Chặn Hiện tại:** Gói sự cố `incidents/Sx/` chưa được phân phối đến repository.
2. **Hành động khi Phát hành:**
   - Chạy `git pull` từ repository upstream.
   - Xác nhận số thẻ với Lab Coach.
   - Thực thi điều tra trace và điền Phần C2 trong `templates/form-c-incident.md` và `reports/t4/C2_incident_error_analysis.md`.
