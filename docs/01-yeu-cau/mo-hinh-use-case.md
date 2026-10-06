# Danh sách Use Case

| Mã UC | Tên UC | Actor chính | Actor phụ | Mô tả ngắn | Ưu tiên |
|-------|--------|-------------|-----------|------------|---------|
| UC-01 | Đăng nhập / Phân quyền | Bạn đọc, Thủ thư, Trưởng TV | Hệ thống | Xác thực tài khoản, phân quyền vai trò. | Cao |
| UC-02 | Tra cứu sách | Bạn đọc | Hệ thống | Tìm đầu sách theo tên/tác giả/ISBN/thể loại. | Cao |
| UC-03 | Mượn sách | Thủ thư | Bạn đọc, Hệ thống | Lập phiếu mượn sau khi kiểm tra điều kiện. | Cao |
| UC-04 | Trả sách | Thủ thư | Bạn đọc, Hệ thống | Ghi nhận trả, cập nhật trạng thái bản sao. | Cao |
| UC-05 | Gia hạn | Thủ thư | Bạn đọc, Hệ thống | Gia hạn tối đa 2 lần × 7 ngày (BR-06). | Cao |
| UC-06 | Đặt trước sách | Bạn đọc | Hệ thống | Đặt trước khi hết bản sao, xếp hàng. | TB |
| UC-07 | Tính tiền phạt | Hệ thống | Thủ thư | Tự động tính phạt 5.000đ/ngày/tài liệu (BR-10). | Cao |
| UC-08 | Thanh toán phạt | Thủ thư | Bạn đọc | Thu tiền phạt, cập nhật công nợ, mở khoá TK. | Cao |
| UC-09 | Quản lý đầu sách/bản sao | Thủ thư | Hệ thống | Thêm/sửa/xoá đầu sách, nhập kho bản sao. | Cao |
| UC-10 | Quản lý bạn đọc | Thủ thư | Hệ thống | Cấp thẻ, gia hạn thẻ, khoá/mở khoá mượn, thu thập email. | Cao |
| UC-11 | Thống kê – báo cáo | Trưởng TV | Hệ thống | Báo cáo mượn/trả/phạt theo kỳ. | TB |
| UC-12 | Nhắc hạn trả tự động | Hệ thống | Bạn đọc | Cron job gửi email nhắc hạn. | TB |
| UC-13 | Kiểm tra quyền và hạn mức mượn | Hệ thống | — | UC include của UC-03, UC-05, UC-06. | Cao |
| UC-14 | Cập nhật trạng thái bản sao | Hệ thống | — | UC include của UC-03, UC-04. | Cao |
