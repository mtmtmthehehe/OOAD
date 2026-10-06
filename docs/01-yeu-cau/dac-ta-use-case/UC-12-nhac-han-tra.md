# UC-12 — Nhắc hạn trả tự động

- **Mã UC:** UC-12
- **Actor chính:** Hệ thống
- **Actor phụ:** Bạn đọc
- **Mô tả:** Cron job chạy 07:00 mỗi ngày: quét phiếu mượn, gửi email nhắc trước hạn 2 ngày và khi quá hạn.
- **Tiền điều kiện:** Không có; do Hệ thống kích hoạt.
- **Hậu điều kiện thành công:** Email nhắc hạn được gửi; phiếu quá hạn chuyển sang trạng thái "Quá hạn".
- **Hậu điều kiện thất bại:** Ghi log lỗi, thử lại lần sau.

## Luồng sự kiện chính
1. 07:00 hàng ngày, cron job quét danh sách phiếu mượn "Đang mượn" và "Trả một phần".
2. Với phiếu có ngày đến hạn = hôm nay + 2: gửi email nhắc lần 1.
3. Với phiếu ngày đến hạn < hôm nay: chuyển trạng thái "Quá hạn" (kể cả phiếu "Trả một phần" còn dòng chưa trả), gửi email cảnh báo.
4. Với phiếu đặt trước quá 3 ngày chưa nhận: tự huỷ, chuyển người kế tiếp.
5. Ghi log kết quả chạy.

## Yêu cầu đặc biệt
- Không bỏ sót phiếu; thử lại khi gửi email lỗi (NFR-08).

## Tần suất: 1 lần/ngày.
