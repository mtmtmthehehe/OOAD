# UC-13 — Kiểm tra quyền & hạn mức

- **Mã UC:** UC-13
- **Actor chính:** Hệ thống
- **Actor phụ:** —
- **Mô tả:** UC include của UC-03/UC-05/UC-06; kiểm tra điều kiện theo ngữ cảnh gọi.
- **Tiền điều kiện:** Có thông tin bạn đọc và ngữ cảnh gọi (`MUON`/`GIA_HAN`/`DAT_TRUOC`).
- **Hậu điều kiện thành công:** Trả về "được phép" kèm lý do.
- **Hậu điều kiện thất bại:** Trả về "từ chối" kèm mã lý do.

## Bảng kiểm tra theo ngữ cảnh

| Kiểm tra | MUON (UC-03) | GIA_HAN (UC-05) | DAT_TRUOC (UC-06) |
|----------|:-:|:-:|:-:|
| Thẻ còn hiệu lực (BR-21) | ✔ | ✔ | ✔ |
| Không bị khoá mượn (BR-13) | ✔ | ✔ | ✔ (BR-23) |
| Công nợ dưới ngưỡng khoá (BR-12, BR-16) | ✔ | ✔ | — |
| Không đang giữ phiếu **nào** quá hạn | ✔ | — (BR-08 chỉ xét phiếu đang gia hạn) | — |
| Hạn mức SV ≤ 5 / GV ≤ 8 (BR-01, BR-02) | ✔ | — | — |

## Luồng sự kiện chính
1. Nhận ngữ cảnh gọi.
2. Thực hiện các kiểm tra bắt buộc theo bảng trên.
3. Trả về kết luận "được phép".

## Luồng thay thế
- 2a. Bất kỳ kiểm tra nào không thoả: trả về "từ chối" với mã lý do tương ứng.

## Tần suất: theo UC-03, UC-05, UC-06.
