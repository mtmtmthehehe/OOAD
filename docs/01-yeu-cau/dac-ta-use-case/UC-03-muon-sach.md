# UC-03 — Mượn sách

- **Mã UC:** UC-03
- **Actor chính:** Thủ thư
- **Actor phụ:** Bạn đọc, Hệ thống
- **Mô tả:** Lập phiếu mượn cho bạn đọc sau khi hệ thống kiểm tra điều kiện và hạn mức.
- **Tiền điều kiện:** Thủ thư đã đăng nhập; bạn đọc xuất trình thẻ thư viện hợp lệ.
- **Hậu điều kiện thành công:** Phiếu mượn được tạo, bản sao chuyển sang "Đang mượn", bạn đọc nhận sách.
- **Hậu điều kiện thất bại:** Không tạo phiếu, không thay đổi trạng thái.

## Luồng sự kiện chính
1. Thủ thư quét/nhập mã thẻ bạn đọc.
2. Hệ thống hiển thị thông tin bạn đọc và danh sách phiếu mượn đang mở.
3. Thủ thư quét/nhập mã các bản sao sách cần mượn.
4. Hệ thống <<include>> UC-13: kiểm tra quyền & hạn mức (thẻ hợp lệ, không nợ phạt, không giữ sách quá hạn, không bị khoá, còn hạn mức mượn).
5. Hệ thống kiểm tra tài liệu không thuộc loại Tham khảo và Tạp chí (BR-05).
6. Hệ thống tính hạn trả: SV 14 ngày, GV 30 ngày (BR-03, BR-04).
7. Thủ thư xác nhận; hệ thống tạo PhieuMuon và ChiTietPhieuMuon.
8. Hệ thống <<include>> UC-14: cập nhật trạng thái bản sao sang "Đang mượn".
9. Bạn đọc ký nhận, nhận sách.

## Luồng thay thế
- 4a. Bạn đọc không đủ điều kiện (nợ phạt/quá hạn/khoá/vượt hạn mức): từ chối mượn, hiển thị lý do.
- 5a. Sách loại Tham khảo hoặc Tạp chí: từ chối mượn về.
- 6a. Sách có người đặt trước mà bạn đọc không phải người đầu hàng: từ chối.

## Luồng ngoại lệ
- Không tìm thấy bản sao: báo lỗi mã sách.

## Yêu cầu đặc biệt
- Hỗ trợ thao tác nhanh giờ cao điểm (NFR-02).

## Tần suất: ~400 lượt/ngày.
