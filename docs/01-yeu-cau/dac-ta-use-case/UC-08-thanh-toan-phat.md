# UC-08 — Thanh toán phạt

- **Mã UC:** UC-08
- **Actor chính:** Thủ thư
- **Actor phụ:** Bạn đọc, Hệ thống
- **Mô tả:** Thu tiền phạt, cập nhật công nợ, mở khoá tài khoản khi đủ điều kiện.
- **Tiền điều kiện:** Bạn đọc có PhieuPhat chưa thanh toán.
- **Hậu điều kiện thành công:** PhieuPhat chuyển "Đã thanh toán" (hoặc "ThanhToanMotPhan"); `so_tien_da_thu` cập nhật; công nợ (dẫn xuất) giảm; mở khoá mượn khi công nợ < ngưỡng khoá (BR-12).
- **Hậu điều kiện thất bại:** Giữ nguyên công nợ.

## Luồng sự kiện chính
1. Bạn đọc yêu cầu thanh toán; thủ thư tra mã thẻ.
2. Hệ thống hiển thị danh sách phiếu phạt chưa trả kèm tổng nợ.
3. Bạn đọc chọn phiếu cần đóng và nộp tiền.
4. Thủ thư xác nhận thu tiền.
5. Hệ thống cập nhật trạng thái "Đã thanh toán" và in biên lai.
6. Hệ thống tính lại công nợ dẫn xuất; nếu dưới ngưỡng khoá (BR-12) và `bi_khoa_muon` đang bật do nợ thì tắt khoá mượn (mở khoá tài khoản bạn đọc).

## Luồng thay thế
- 3a. Thanh toán một phần: cộng `so_tien_da_thu`, trạng thái thành "ThanhToanMotPhan" (enum TrangThaiPhat). Công nợ dẫn xuất = Σ(so_tien − so_tien_da_thu).

## Tần suất: ~40 lượt/ngày.
