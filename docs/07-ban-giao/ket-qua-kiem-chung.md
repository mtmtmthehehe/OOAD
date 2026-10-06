# Kết quả kiểm chứng

Ngày chạy: 06/10/2026. Commit: sẽ cập nhật sau khi commit cuối.

## `bash scripts/check.sh`
- 1. Bảng lệch cột: không có.
- 2. Truy vết: BR 23, FR 23, NFR 9, UC 14, CLS 23, TC 60 — mọi TC khớp hàng ma trận, mọi BR/FR có TC, mọi FR khớp bảng phụ/BR gốc, ID tồn tại, link không hỏng, PNG mới hơn PML.
- 3. Cú pháp PlantUML: toàn bộ `.puml` hợp lệ.
- 4. Số liệu nghiệp vụ ngoài file nguồn đều kèm mã BR cùng dòng: không dòng nào vi phạm.

## Render PNG
10 file HTML render thành công (PlantUML + graphviz), kích thước tham khảo ~ 168k CTX cho một lần review toàn bộ.

## Chưa có (thuộc giai đoạn thi công)
- Kiểm thử cạnh tranh CSDL, tải, UAT, phục hồi thảm hoạ.
