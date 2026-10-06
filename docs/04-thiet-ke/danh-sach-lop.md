# Danh sách lớp thiết kế

| Mã lớp | Tên lớp | Loại | Trách nhiệm | UC liên quan |
|--------|---------|------|-------------|--------------|
| CLS-01 | DauSach | Entity | Thông tin đầu sách, tìm kiếm | UC-02, UC-06, UC-09 |
| CLS-02 | BanSaoSach | Entity | Trạng thái bản sao, vị trí kệ | UC-03, UC-04, UC-06, UC-09 |
| CLS-03 | BanDoc | Entity | Thông tin bạn đọc, điều kiện mượn, công nợ | UC-03, UC-05, UC-08, UC-10 |
| CLS-04 | TheThuVien | Entity | Quản lý thẻ thư viện | UC-01, UC-10, UC-13 |
| CLS-05 | PhieuMuon | Entity | Phiếu mượn, hạn trả lưu (tính lúc tạo, cập nhật khi gia hạn), gia hạn | UC-03, UC-04, UC-05, UC-12 |
| CLS-06 | ChiTietPhieuMuon | Entity | Chi tiết từng bản sao trong phiếu | UC-03, UC-04, UC-05, UC-07 |
| CLS-07 | PhieuPhat | Entity | Tính và ghi nhận tiền phạt | UC-04, UC-07, UC-08 |
| CLS-08 | PhieuDatTruoc | Entity | Hàng đợi đặt trước | UC-06, UC-12 |
| CLS-09 | ThuThu | Entity | Thông tin thủ thư | UC-03, UC-04, UC-09, UC-10 |
| CLS-10 | NhaXuatBan | Entity | Thông tin NXB | UC-09 |
| CLS-11 | TacGia | Entity | Thông tin tác giả | UC-02, UC-09 |
| CLS-12 | TheLoai | Entity | Phân loại thể loại sách | UC-02, UC-09 |
| CLS-13 | ManHinhMuonSach | Boundary | Giao diện mượn | UC-03 |
| CLS-14 | ManHinhTraSach | Boundary | Giao diện trả | UC-04 |
| CLS-15 | ManHinhGiaHan | Boundary | Giao diện gia hạn | UC-05 |
| CLS-16 | ManHinhTraCuu | Boundary | Giao diện tra cứu/đặt trước | UC-02, UC-06 |
| CLS-17 | ControllerMuonSach | Control | Điều phối luồng mượn | UC-03 |
| CLS-18 | ControllerTraSach | Control | Điều phối luồng trả + phạt | UC-04, UC-07 |
| CLS-19 | ControllerGiaHan | Control | Điều phối luồng gia hạn | UC-05 |
| CLS-20 | ControllerDatTruoc | Control | Điều phối luồng đặt trước | UC-06 |
| CLS-21 | TaiKhoan | Entity | Tài khoản đăng nhập, vai trò, trạng thái HoatDong/VoHieuHoa | UC-01 |
| CLS-22 | NhatKy | Entity | Ghi log thao tác | UC-01, UC-03, UC-04 |
| CLS-23 | ManHinhDatTruoc | Boundary | Màn hình đặt trước (tách từ UC-06) | UC-06 |
| CLS-24 | ThanhToanPhat | Entity | Lịch sử từng lần thu phạt, phục vụ biên lai | UC-08 |
