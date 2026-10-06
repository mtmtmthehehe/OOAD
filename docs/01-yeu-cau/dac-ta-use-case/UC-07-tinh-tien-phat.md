# UC-07 — Tính tiền phạt

- **Mã UC:** UC-07
- **Actor chính:** Hệ thống
- **Actor phụ:** Thủ thư
- **Mô tả:** Tính tiền phạt quá hạn theo từng dòng chi tiết phiếu mượn.
- **Tiền điều kiện:** Có ít nhất một dòng `ChiTietPhieuMuon` trả trễ.
- **Hậu điều kiện thành công:** PhieuPhat được tạo với số tiền đúng theo BR.
- **Hậu điều kiện thất bại:** Không tạo phiếu phạt.

## Luồng sự kiện chính
1. Khi trả sách (UC-04), với mỗi dòng chi tiết được ghi nhận trả:
2. Hệ thống tính số ngày trễ = max(0, ngày thực trả − ngày đến hạn) cho riêng dòng đó (BR-11).
3. Nếu ngày trễ > 0: phạt_dòng = 5.000đ × ngày trễ (BR-10, Q5).
4. Tổng phạt = Σ phạt_dòng; tạo PhieuPhat tương ứng (trạng thái ChuaThanhToan, `so_tien_da_thu` = 0).
5. Công nợ (dẫn xuất) = Σ(so_tien − so_tien_da_thu) các phiếu phạt chưa hoàn; nếu ≥ 100.000đ thì bật `bi_khoa_muon` (BR-12, BR-13).

## Luồng thay thế
- 2a. Trả đúng hạn hoặc sớm: không phát sinh phạt cho dòng đó.

## Ví dụ minh hoạ
- Hai cuốn trả cùng ngày, cùng trễ 4 ngày → tổng = 2 × (5.000 × 4) = 40.000đ. (BR-10)
- Hai cuốn trả lệch ngày (trễ 4 và 2 ngày) → tổng = 5.000 × (4 + 2) = 30.000đ. (BR-10)

## Tần suất: ~60 lượt/ngày.
