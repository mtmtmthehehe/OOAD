# UC-10 — Quản lý bạn đọc

- **Mã UC:** UC-10
- **Actor chính:** Thủ thư
- **Actor phụ:** Hệ thống
- **Mô tả:** Cấp thẻ, gia hạn thẻ, khoá/mở tài khoản bạn đọc, thu thập email.
- **Tiền điều kiện:** Thủ thư đăng nhập.
- **Hậu điều kiện thành công:** Thông tin BanDoc/TheThuVien cập nhật.
- **Hậu điều kiện thất bại:** Không thay đổi dữ liệu.

## Luồng sự kiện chính
1. Thủ thư chọn chức năng quản lý bạn đọc.
2. Hệ thống hiển thị danh sách bạn đọc.
3. Thủ thư thêm mới/cập nhật/khoá/mở tài khoản.
4. Hệ thống kiểm tra dữ liệu hợp lệ (mã số SV/GV duy nhất, email đúng định dạng — bắt buộc vì UC-12/FR-19 gửi email, F1).
6. Luồng gia hạn thẻ: thủ thư chọn bạn đọc → nhập ngày hết hạn mới (ngày cấp + 12 tháng theo BR-21) → lưu. Thẻ quá 12 tháng bị từ chối mượn (TC-44).
5. Hệ thống lưu thay đổi.

## Luồng thay thế
- 4a. Mã SV/GV trùng: từ chối.
- 3a. Mở khoá tài khoản còn nợ ≥ 100.000đ: từ chối, yêu cầu đóng phạt trước (BR-13).

## Tần suất: ~15 lượt/ngày.
