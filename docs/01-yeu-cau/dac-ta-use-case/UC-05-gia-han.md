# UC-05 — Gia hạn mượn

- **Mã UC:** UC-05
- **Actor chính:** Thủ thư
- **Actor phụ:** Bạn đọc, Hệ thống
- **Mô tả:** Kéo dài thời hạn mượn nếu đủ điều kiện: tối đa 2 lần, mỗi lần 7 ngày (BR-06).
- **Tiền điều kiện:** Phiếu mượn đang ở trạng thái "Đang mượn".
- **Hậu điều kiện thành công:** Ngày đến hạn mới = ngày đến hạn cũ + 7 ngày (BR-06); số lần gia hạn tăng 1.
- **Hậu điều kiện thất bại:** Giữ nguyên hạn trả, hiển thị lý do.

## Luồng sự kiện chính
1. Bạn đọc yêu cầu gia hạn; thủ thư nhập mã phiếu.
2. Hệ thống hiển thị thông tin phiếu: số lần đã gia hạn, ngày đến hạn.
3. Hệ thống kiểm tra số lần gia hạn < 2 (BR-06).
4. Hệ thống <<include>> UC-13 (ngữ cảnh GIA_HAN): thẻ còn hạn, không bị khoá mượn, công nợ dưới ngưỡng. Không kiểm hạn mức/quá hạn khác (Q2).
5. Hệ thống kiểm tra còn ≥ 2 ngày trước hạn (BR-07) và phiếu chưa quá hạn (BR-08).
6. Hệ thống kiểm tra không có đặt trước cho bản sao (BR-09).
7. Hệ thống cập nhật ngày đến hạn mới (+7 ngày, BR-06).

## Luồng thay thế
- 3a. Đã gia hạn 2 lần: từ chối (BR-06).
- 5a. Đã quá hạn hoặc còn < 2 ngày: từ chối.
- 6a. Có người đặt trước: từ chối gia hạn.

## Luồng ngoại lệ
- Phiếu không tồn tại: báo lỗi.

## Tần suất: ~120 lượt/ngày.
