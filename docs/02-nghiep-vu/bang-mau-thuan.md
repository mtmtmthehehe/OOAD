# Bảng mâu thuẫn và phương án xử lý

| Mâu thuẫn | Mô tả | Phương án xử lý | Người quyết định | Ngày chốt |
|-----------|-------|------------------|-------------------|-----------|
| Tính phạt theo ngày lịch hay ngày làm việc | Thủ thư nói tính theo ngày lịch (kể cả Chủ nhật), quy định cũ ghi theo ngày làm việc của thư viện. | Thống nhất tính theo **ngày lịch** vì đơn giản, dễ kiểm tra, hạn chế khiếu nại. | Trưởng thư viện | 06/10/2026 |
| Mốc được phép gia hạn | Thủ thư đề xuất gia hạn bất cứ lúc nào; Trưởng thư viện yêu cầu phải còn ≥ 2 ngày trước hạn. | Chọn mốc **trước hạn ≥ 2 ngày** (BR-07), thống nhất với BR trong quy-tac-nghiep-vu. | Trưởng thư viện | 06/10/2026 |
| Số lần gia hạn tối đa | Một số ý kiến cho gia hạn không giới hạn đến khi có người đặt trước. | Chốt **tối đa 2 lần, mỗi lần 7 ngày** (BR-06). | Trưởng thư viện | 06/10/2026 |
| Ngưỡng khoá tài khoản | Ý kiến 50.000đ vs 200.000đ. | Chốt **100.000đ** (BR-12). | Trưởng thư viện | 06/10/2026 |

Tất cả quyết định trên đã được đồng bộ vào quy-tac-nghiep-vu, yeu-cau-chuc-nang, đặc tả UC và biểu đồ.

## Nguồn tham khảo các số liệu BR
- Biên bản phỏng vấn: `bien-ban-phong-van.md`
- Bảng luật nghiệp vụ đầy đủ tại `quy-tac-nghiep-vu.md`

## Quyết định đã chốt (Q1–Q9)

| Mã | Quyết định |
|----|------------|
| Q1 | BR-20 chỉ giới hạn phạt trễ hạn; không áp đền bù mất/hỏng (BR-14/15). |
| Q2 | UC-13 tham số hoá kiểm tra theo ngữ cảnh MUON / GIA_HAN / DAT_TRUOC (bảng trong đặc tả UC-13). |
| Q3 | Tài khoản bị khoá không được đặt trước (BR-23 mới). |
| Q4 | Loại `TapChi` không cho mượn về (mở rộng BR-05). |
| Q5 | Phạt tính theo từng dòng chi tiết: 5.000đ × (ngày thực trả − ngày đến hạn) mỗi dòng; tổng = Σ. |
| Q6 | Cho thanh toán phạt một phần; `phieu_phat` thêm `so_tien_da_thu`. |
| Q7 | `cong_no` là dẫn xuất: Σ(so_tien − so_tien_da_thu) của phiếu phạt chưa đủ. |
| Q8 | "Khoá" tách 2: `tai_khoan.trang_thai` (HoatDong/VoHieuHoa, chặn đăng nhập) và `ban_doc.bi_khoa_muon` (khoá mượn/gia hạn/đặt trước do nợ). Bị khoá mượn vẫn đăng nhập, tra cứu, trả sách, nộp phạt. |
| Q9 | Mã bản sao dạng `<XXX>-<dddd>` (XXX = mã đầu sách rút gọn 3 ký tự, dddd = 4 số), ví dụ LTJ-0012. |
