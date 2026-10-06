# UC-06 — Đặt trước sách

- **Mã UC:** UC-06
- **Actor chính:** Bạn đọc
- **Actor phụ:** Hệ thống
- **Mô tả:** Đặt trước đầu sách khi không còn bản sao nào "Có sẵn"; hệ thống xếp hàng tự động.
- **Tiền điều kiện:** Bạn đọc đăng nhập; đầu sách không còn bản sao trống.
- **Hậu điều kiện thành công:** PhieuDatTruoc được tạo với vị trí hàng đợi; khi đến lượt, bạn đọc được giữ sách 3 ngày.
- **Hậu điều kiện thất bại:** Không tạo phiếu.

## Luồng sự kiện chính
1. Bạn đọc tìm sách ở UC-02, chọn "Đặt trước".
2. Hệ thống kiểm tra tất cả bản sao đều không "Có sẵn".
3. Hệ thống kiểm tra bạn đọc chưa có phiếu đặt trước trùng đầu sách này, và số phiếu đặt trước đang chờ < 2 (BR-19).
4. Hệ thống <<include>> UC-13 (ngữ cảnh DAT_TRUOC): thẻ còn hạn, không bị khoá mượn (BR-23); KHÔNG kiểm hạn mức mượn hay phiếu quá hạn (Q2). Rồi tạo PhieuDatTruoc, viTriHang = vị trí cuối hàng đợi (BR-17).
5. Hệ thống xác nhận và hiển thị vị trí hàng đợi.

## Luồng thay thế
- 2a. Còn bản sao "Có sẵn": gợi ý mượn trực tiếp.
- 3a. Đã có phiếu đặt trước trùng đầu sách: từ chối.
- 3b. Đang có 2 phiếu đặt trước chờ: từ chối (BR-19).

## Luồng thay thế (khi sách trả về)
- Khi bản sao trả về, hệ thống chuyển người đầu hàng đợi thành "Đã sẵn sàng nhận", giữ 3 ngày (BR-18); quá 3 ngày tự huỷ và chuyển người kế tiếp, bản sao trả về trạng thái "Có sẵn".

## Tần suất: ~80 lượt/ngày.
