# Thiết kế giao diện (Wireframe mô tả vùng)

## 1. Màn hình Đăng nhập
- Vùng 1: Logo + tên thư viện
- Vùng 2: Form nhập Tên đăng nhập / Mật khẩu
- Vùng 3: Nút "Đăng nhập" + link "Quên mật khẩu"
- UC: UC-01

## 2. Trang chủ Thủ thư
- Vùng 1 (top): Thanh menu — Mượn/Trả, Bạn đọc, Đầu sách, Báo cáo
- Vùng 2 (trái): Tra cứu nhanh theo mã thẻ/mã sách
- Vùng 3 (giữa): Danh sách phiếu mượn quá hạn hôm nay
- Vùng 4 (phải): Thông báo hệ thống
- UC: UC-03, UC-04, UC-08, UC-09, UC-10

## 3. Màn hình Tra cứu sách
- Vùng 1: Ô tìm kiếm (tên/tác giả/ISBN/thể loại)
- Vùng 2: Bộ lọc (Năm XB, NXB, Thể loại)
- Vùng 3: Bảng kết quả: Tên | Tác giả | Thể loại | Tình trạng | Vị trí kệ
- Vùng 4: Nút "Đặt trước" / "Chi tiết"
- UC: UC-02, UC-06

## 4. Màn hình Mượn/Trả
- Vùng 1: Quét mã thẻ bạn đọc → hiển thị thông tin + công nợ
- Vùng 2: Danh sách sách đang quét, hạn trả dự kiến
- Vùng 3: Nút "Xác nhận mượn" / "Trả sách" / "Gia hạn"
- Vùng 4: Cảnh báo (quá hạn, công nợ vượt ngưỡng khoá theo BR-12)
- UC: UC-03, UC-04, UC-05

## 5. Màn hình Quản lý bạn đọc
- Vùng 1: Tìm kiếm bạn đọc
- Vùng 2: Bảng: Mã | Họ tên | Loại | Công nợ | Trạng thái | Thao tác
- Vùng 3: Nút thêm mới / khoá / mở khoá / gia hạn thẻ
- UC: UC-10

## 6. Màn hình Thống kê – báo cáo
- Vùng 1: Chọn loại báo cáo + khoảng thời gian
- Vùng 2: Biểu đồ cột (lượt mượn theo tháng)
- Vùng 3: Bảng top 10 sách mượn nhiều, tổng nợ phạt
- Vùng 4: Nút xuất Excel/PDF (UC-11, FR-23)
- UC: UC-11

## 7. Màn hình Thanh toán phạt (UC-08)
- Vùng 1: Tìm bạn đọc theo mã thẻ/tên.
- Vùng 2: Bảng phiếu phạt chưa thanh toán: Mã phiếu | Loại | Số tiền | Đã thu | Còn nợ | Chọn.
- Vùng 3: Nhập số tiền thanh toán (hỗ trợ một phần) + xác nhận.
- Vùng 4: Bảng lịch sử thanh toán + nút in biên lai.

## 8. Màn hình Quản lý đầu sách & bản sao (UC-09)
- Vùng 1: Bộ lọc đầu sách (tên, tác giả, thể loại, NXB).
- Vùng 2: Bảng đầu sách + nút Thêm/Sửa/Xoá.
- Vùng 3: Danh sách bản sao của đầu sách đang chọn; nút Nhập kho bản sao (sinh mã theo BR-22).
- Vùng 4: Vị trí giá kệ mỗi bản sao.

## 9. Màn hình Đặt trước của Bạn đọc (UC-06)
- Vùng 1: Ô tìm đầu sách (dùng kết quả từ màn hình Tra cứu).
- Vùng 2: Nút "Đặt trước" kèm điều kiện: không còn bản sao "Có sẵn", tài khoản không bị khoá (BR-23).
- Vùng 3: Bảng đặt trước của tôi: Mã đầu sách | Vị trí hàng | Trạng thái (DangCho/SanSangNhan/DaNhan/DaHuy) | Hạn nhận (BR-18).

## 10. Trang chủ Bạn đọc
- Vùng 1: Lời chào + số sách đang mượn, số phiếu quá hạn.
- Vùng 2: Bảng "Sách đang mượn": Mã sách | Hạn trả | Gia hạn (lần/2 theo BR-06).
- Vùng 3: Công nợ hiện tại (dẫn xuất, Q7) — hiển thị giá trị tính từ phiếu phạt.
- Vùng 4: Menu: Tra cứu, Đặt trước của tôi, Lịch sử.

## 11. Trang chủ Trưởng thư viện
- Vùng 1: Bộ lọc thời gian.
- Vùng 2: Biểu đồ lượt mượn/trả theo tháng (nguồn: PhieuMuon, ChiTietPhieuMuon).
- Vùng 3: Top đầu sách mượn nhiều; tổng công nợ; số bạn đọc bị khoá (BR-12).
- Vùng 4: Nút xuất Excel/PDF (FR-23).
