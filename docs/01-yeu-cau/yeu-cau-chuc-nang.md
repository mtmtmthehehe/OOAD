# Yêu cầu chức năng (FR)

| Mã FR | Mô tả | Ưu tiên | BR gốc |
|-------|-------|---------|--------|
| FR-01 | Đăng nhập, phân quyền theo vai trò (Bạn đọc / Thủ thư / Trưởng thư viện / Hệ thống). | Cao | — |
| FR-02 | Tra cứu đầu sách theo tên, tác giả, thể loại, ISBN. | Cao | — |
| FR-03 | Thủ thư lập phiếu mượn cho bạn đọc sau khi kiểm tra điều kiện. | Cao | BR-16 |
| FR-04 | Kiểm tra hạn mức mượn theo loại đối tượng (SV ≤ 5, GV ≤ 8). | Cao | BR-01, BR-02 |
| FR-05 | Tính hạn trả tự động: SV 14 ngày, GV 30 ngày. | Cao | BR-03, BR-04 |
| FR-06 | Ngăn mượn tài liệu loại tham khảo tại chỗ và Tạp chí. | Cao | BR-05 |
| FR-07 | Gia hạn phiếu mượn tối đa 2 lần, mỗi lần 7 ngày. | Cao | BR-06 |
| FR-08 | Kiểm tra điều kiện gia hạn (trước hạn ≥ 2 ngày, chưa quá hạn, chưa có người đặt trước). | Cao | BR-07, BR-08, BR-09 |
| FR-09 | Ghi nhận trả sách từng dòng chi tiết, cập nhật trạng thái bản sao và phiếu mượn. | Cao | — |
| FR-10 | Tính tiền phạt quá hạn 5.000đ/ngày/tài liệu. | Cao | BR-10, BR-11 |
| FR-11 | Khoá mượn/gia hạn/đặt trước khi nợ phạt ≥ 100.000đ và mở lại sau khi thanh toán. | Cao | BR-12, BR-13 |
| FR-12 | Tính đền bù mất/hư hỏng (2× giá bìa / 50% giá bìa). | Cao | BR-14, BR-15 |
| FR-13 | Đặt trước tài liệu khi hết, xếp hàng theo thời gian. | TB | BR-17, BR-23 |
| FR-14 | Thông báo và huỷ phiếu đặt trước nếu quá 3 ngày không nhận. | TB | BR-18 |
| FR-15 | Giới hạn tối đa 2 phiếu đặt trước chưa đến lượt/bạn đọc. | TB | BR-19 |
| FR-16 | Quản lý đầu sách: thêm/sửa/xoá, nhập kho bản sao. | Cao | BR-22 |
| FR-17 | Quản lý bạn đọc: cấp thẻ, khoá/mở tài khoản, xem lịch sử. | Cao | BR-12, BR-13, BR-21 |
| FR-18 | Thống kê – báo cáo: đầu sách mượn nhiều, nợ phạt, trả muộn. | TB | — |
| FR-19 | Nhắc hạn trả tự động (cron job, gửi email) trước hạn 2 ngày. | TB | — |
| FR-20 | Tìm kiếm nâng cao theo năm xuất bản, nhà xuất bản. | Thấp | — |
| FR-21 | Xuất phiếu mượn/trả dưới dạng PDF. | Thấp | — |
| FR-23 | Xuất báo cáo ra Excel/PDF. | Thấp | — |
| FR-22 | Giới hạn tiền phạt trễ hạn tối đa bằng tổng giá bìa tài liệu trong phiếu. | Cao | BR-20 |

