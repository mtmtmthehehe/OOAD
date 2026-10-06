# Yêu cầu phi chức năng (NFR)

| Mã NFR | Mô tả | Loại |
|--------|-------|------|
| NFR-01 | Tra cứu sách trả kết quả trong ≤ 2 giây với ~18.000 đầu sách. | Hiệu năng |
| NFR-02 | Hỗ trợ ≥ 50 người dùng đồng thời truy cập. | Đồng thời |
| NFR-03 | Mật khẩu lưu dạng băm, phân quyền chặt theo vai trò. | Bảo mật |
| NFR-04 | Sao lưu CSDL tự động hàng ngày, giữ 30 bản gần nhất. | Sao lưu |
| NFR-05 | Thời gian phản hồi thao tác mượn/trả ≤ 3 giây. | Hiệu năng |
| NFR-06 | Kiến trúc 3 lớp cho phép mở rộng thêm chi nhánh thư viện. | Khả năng mở rộng |
| NFR-07 | Giao diện tiếng Việt, tương thích Chrome/Edge mới nhất. | Khả năng sử dụng |
| NFR-08 | Cron job nhắc hạn chạy ổn định 1 lần/ngày lúc 07:00. | Khả năng vận hành |
| NFR-09 | Nhập sai mật khẩu 3 lần liên tiếp: tạm khoá đăng nhập 15 phút; hết thời gian mới thử lại được. | Bảo mật |
