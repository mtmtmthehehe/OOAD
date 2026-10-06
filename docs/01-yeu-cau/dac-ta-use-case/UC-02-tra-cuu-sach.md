# UC-02 — Tra cứu sách

- **Mã UC:** UC-02
- **Actor chính:** Bạn đọc
- **Actor phụ:** Hệ thống
- **Mô tả:** Tìm kiếm đầu sách theo tên, tác giả, thể loại, ISBN và xem tình trạng các bản sao.
- **Tiền điều kiện:** Người dùng đã đăng nhập (UC-01).
- **Hậu điều kiện thành công:** Hiển thị danh sách kết quả kèm trạng thái bản sao (Có sẵn/Đang mượn/Đã đặt trước/Mất/Hư hỏng).
- **Hậu điều kiện thất bại:** Không thay đổi dữ liệu.

## Luồng sự kiện chính
1. Bạn đọc nhập từ khoá tìm kiếm.
2. Hệ thống thực hiện tìm kiếm trong CSDL.
3. Hệ thống hiển thị danh sách đầu sách phù hợp.
4. Bạn đọc chọn một đầu sách để xem chi tiết (vị trí giá kệ, số bản sao, tình trạng — gồm cả "Mất" và "Đã đặt trước").

## Luồng thay thế
- 2a. Không có kết quả: hệ thống thông báo "Không tìm thấy", gợi ý từ khoá khác.

## Luồng ngoại lệ
- Lỗi kết nối: thông báo lỗi, ghi log.

## Yêu cầu đặc biệt
- Kết quả trả về ≤ 2 giây với 18.000 đầu sách (NFR-01).

## Tần suất: ~500 lượt/ngày.
