# UC-11 — Thống kê – báo cáo

- **Mã UC:** UC-11
- **Actor chính:** Trưởng thư viện
- **Actor phụ:** Hệ thống
- **Mô tả:** Xem và xuất báo cáo mượn/trả/phạt theo tháng hoặc theo khoảng thời gian.
- **Tiền điều kiện:** Trưởng thư viện đăng nhập.
- **Hậu điều kiện thành công:** Hiển thị biểu đồ/bảng số liệu, có thể xuất Excel.
- **Hậu điều kiện thất bại:** Không thay đổi dữ liệu.

## Luồng sự kiện chính
1. Trưởng thư viện chọn loại báo cáo và khoảng thời gian.
2. Hệ thống tổng hợp dữ liệu từ PhieuMuon, ChiTietPhieuMuon (ghi nhận trả) và PhieuPhat.
3. Hệ thống hiển thị kết quả dạng bảng và biểu đồ.
4. Người dùng có thể xuất file.

## Luồng thay thế
- 2a. Không có dữ liệu trong kỳ: hiển thị "Không có dữ liệu".

## Tần suất: ~5 lượt/ngày.
