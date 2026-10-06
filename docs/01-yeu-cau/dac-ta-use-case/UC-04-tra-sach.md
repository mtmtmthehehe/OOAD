# UC-04 — Trả sách

- **Mã UC:** UC-04
- **Actor chính:** Thủ thư
- **Actor phụ:** Bạn đọc, Hệ thống
- **Mô tả:** Ghi nhận trả sách, tính phạt/đền nếu có, cập nhật trạng thái bản sao, đóng phiếu khi hết dòng chưa trả.
- **Tiền điều kiện:** Bạn đọc có phiếu mượn đang mở.
- **Hậu điều kiện thành công:** Dòng chi tiết ghi nhận `ngayTra`; bản sao → "Có sẵn" / "Đã đặt trước" / "Hư hỏng" / "Mất"; phiếu đóng khi mọi dòng đã trả; phiếu phạt tạo khi có phát sinh.
- **Hậu điều kiện thất bại:** Không thay đổi dữ liệu.

## Luồng sự kiện chính
1. Thủ thư quét mã bản sao trả.
2. Hệ thống hiển thị phiếu mượn tương ứng và ngày đến hạn của dòng đó.
3. Thủ thư kiểm tra tình trạng sách (bình thường / hư hỏng / mất).
4. Thủ thư xác nhận; hệ thống ghi `ngayTra` cho dòng `ChiTietPhieuMuon`.
5. Theo kết quả kiểm tra ở bước 3, hệ thống phát sinh phiếu phạt tương ứng (bước 6a/6b) nếu có.
6. Hệ thống <<include>> UC-14: cập nhật trạng thái bản sao:
   - Nếu có người đặt trước đang chờ cho đầu sách → "Đã đặt trước" (BR-18); phiếu người đầu hàng → "Sẵn sàng nhận" và gửi email thông báo (FR-14).
   - Ngược lại → "Có sẵn".
7. Nếu mọi dòng trong phiếu đã có `ngayTra` → đóng phiếu mượn (`DaTra` / `DaTraTre` / `MatHuHong`). Nếu còn dòng chưa trả → phiếu giữ trạng thái `TraMotPhan` (hoặc giữ `QuaHan` nếu đã quá hạn).

## Luồng thay thế
- 5a. Sách trả trễ: hệ thống <<extend>> UC-07, tính phạt riêng cho dòng này (5.000đ × ngày trễ, BR-10).
- 5b. Sách hư hỏng: thêm phiếu phạt loại HONG = 50% giá bìa (BR-15); bản sao → "Hư hỏng".
- 5c. Sách mất: thêm phiếu phạt loại MAT = 2 × giá bìa (BR-14); bản sao → "Mất".
- 5d. Một dòng có thể vừa trễ vừa mất/hỏng: hệ thống tạo 2 phiếu phạt độc lập (TRE + MAT/HONG).
- Trả một phần: thủ thư chỉ ghi `ngayTra` cho các dòng trả; phiếu giữ `TraMotPhan`.

## Luồng ngoại lệ
- Bản sao không thuộc phiếu mượn đang mở: cảnh báo.

## Yêu cầu đặc biệt
- Phạt tính theo ngày lịch, theo từng dòng chi tiết (BR-10, BR-11, Q5).

## Tần suất: ~350 lượt/ngày.
