# UC-14 — Cập nhật trạng thái bản sao

- **Mã UC:** UC-14
- **Actor chính:** Hệ thống
- **Actor phụ:** —
- **Mô tả:** UC include của UC-03/UC-04; cập nhật trạng thái BanSaoSach theo sự kiện.
- **Tiền điều kiện:** Có bản sao liên quan.
- **Hậu điều kiện thành công:** Trạng thái bản sao được cập nhật đúng vòng đời.
- **Hậu điều kiện thất bại:** Không thay đổi trạng thái.

## Luồng sự kiện chính
1. Nhận sự kiện: mượn → chuyển "Có sẵn" → "Đang mượn".
2. Trả → chuyển "Đang mượn" → "Có sẵn".
3. Ghi nhận mất → chuyển "Mất"; hư hỏng → "Hư hỏng".
4. Có đặt trước đang chờ cho đầu sách → chuyển về "Đã đặt trước" (sự kiện kích hoạt: UC-04 khi bản sao vừa được trả). UC-06 tạo phiếu đặt trước KHÔNG đổi trạng thái bản sao; UC-03 đặt trạng thái "Đang mượn".

## Tần suất: theo UC-03, UC-04.
