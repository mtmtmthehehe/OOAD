# Kết quả kiểm chứng

Ngày chạy: 06/10/2026. Base commit: `0ef2cbf` (các thay đổi sau đó chưa commit tại thời điểm chạy).

## `bash scripts/check.sh` — exit code 0
- 1. Bảng lệch cột: không có.
- 2. Truy vết: `Truy vết OK: BR 23 FR 23 NFR 9 UC 14 CLS 23 TC 60` — mọi TC khớp hàng ma trận, mọi BR/FR có TC, FR khớp bảng phụ/BR gốc, ID tồn tại, link nội bộ không hỏng, PNG được render lại cùng `.puml` (so theo git working tree).
- 3. Cú pháp PlantUML: toàn bộ `.puml` hợp lệ.
- 4. Các con số nghiệp vụ nằm ngoài file nguồn đều kèm mã BR hoặc mã quyết định Qn cùng dòng: không dòng nào vi phạm.

## Render PNG
`bash scripts/render-all.sh` (PlantUML + Graphviz) tạo lại 10 file PNG từ `.puml`.

## Giới hạn đã biết
- Số liệu nghiệp vụ là đề xuất/giả định của nhóm, chưa có văn bản xác nhận từ Phòng QL Thư viện (xem `quy-tac-nghiep-vu.md`).
- Chưa có kiểm thử CSDL, tải, UAT, phục hồi thảm hoạ (thuộc giai đoạn thi công).
