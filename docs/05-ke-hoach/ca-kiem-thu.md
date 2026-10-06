# Ca kiểm thử (Test Cases)

| Mã TC | UC | BR/FR liên quan | Tiền điều kiện | Dữ liệu vào | Kết quả mong đợi |
|-------|----|----------------|----------------|-------------|------------------|
| TC-01 | UC-01 | FR-01 | Có TK hoạt động | user=sv01, pass=Matkhau@123 | Đăng nhập thành công |
| TC-02 | UC-01 | FR-01 | Có TK hoạt động | pass=Saimatkhau | Báo lỗi, cho nhập lại tối đa 3 lần |
| TC-03 | UC-02 | FR-02 | Đã đăng nhập | tuKhoa="Lập trình Java" | Trả kết quả ≤ 2s |
| TC-04 | UC-02 | FR-02 | Đã đăng nhập | tuKhoa="xyzabc" | "Không tìm thấy" |
| TC-05 | UC-03 | BR-03, FR-05 | SV hợp lệ, đang giữ 0 cuốn | 2 bản sao "Có sẵn", loại GiaoTrinh | Tạo phiếu, hạn trả = ngày mượn + 14 |
| TC-06 | UC-03 | BR-01, FR-04 | SV đang giữ 5 cuốn | Xin mượn cuốn thứ 6 | Từ chối, báo vượt hạn mức SV |
| TC-07 | UC-03 | BR-04, FR-05 | GV hợp lệ, đang giữ 0 cuốn | 3 bản sao "Có sẵn" | Hạn trả = ngày mượn + 30 |
| TC-08 | UC-03 | BR-05, FR-06 | Bạn đọc hợp lệ | mã sách loại ThamKhao | Từ chối mượn về |
| TC-09 | UC-03 | BR-16, FR-03 | Bạn đọc nợ phạt 120.000đ | — | Từ chối, yêu cầu đóng phạt |
| TC-10 | UC-04 | FR-09 | Phiếu mượn đang mở, đúng hạn | ngayTra = ngayDenHan | Đóng phiếu, bản sao → CoSan |
| TC-11 | UC-04 | BR-10, BR-11, FR-10 | Trả trễ | tre 4 ngày, 2 cuốn, trả cùng ngày | Phạt = 5.000 × 4 × 2 = 40.000đ (theo từng dòng, Q5) |
| TC-12 | UC-04 | BR-15, FR-12 | Sách hư hỏng, giá bìa 80.000đ | biên bản hỏng | Phạt = 40.000đ |
| TC-13 | UC-04 | BR-14, FR-12 | Sách mất, giá bìa 100.000đ | báo mất | Đền 200.000đ hoặc sách thay thế |
| TC-14 | UC-05 | BR-06, FR-07 | Đã gia hạn 1 lần, còn 5 ngày | — | Hạn mới = hạn cũ + 7 |
| TC-15 | UC-05 | BR-06, FR-07 | Đã gia hạn 2 lần | xin lần 3 | Từ chối |
| TC-16 | UC-05 | BR-07, FR-08 | Còn 1 ngày trước hạn | — | Từ chối |
| TC-17 | UC-05 | BR-08, FR-08 | Phiếu đã quá hạn | ngayHienTai > ngayDenHan | Từ chối |
| TC-18 | UC-05 | BR-09, FR-08 | Sách có người đặt trước | hàng đợi ≠ rỗng | Từ chối gia hạn |
| TC-19 | UC-06 | BR-17, FR-13 | Sách hết bản sao "Có sẵn" | — | Tạo phiếu, viTriHang = cuối hàng |
| TC-20 | UC-06 | FR-13 | Sách còn bản sao "Có sẵn" | — | Gợi ý mượn trực tiếp |
| TC-21 | UC-06 | BR-18, FR-14 | Đến lượt, quá 3 ngày không nhận | ngayQua = 3 ngày | Huỷ phiếu, chuyển người kế tiếp |
| TC-22 | UC-08 | BR-12, BR-13, FR-11 | Nợ 150.000đ, TK bị khoá | thanh toán 150.000đ | Công nợ = 0, mở khoá TK |
| TC-23 | UC-08 | BR-13, FR-11 | Nợ 150.000đ | thanh toán 50.000đ | Công nợ = 100.000đ, TK vẫn khoá |
| TC-24 | UC-12 | FR-19 | Phiếu còn 2 ngày đến hạn | cron 07:00 | Gửi email nhắc hạn |
| TC-25 | UC-12 | FR-19 | Phiếu quá hạn 1 ngày | cron 07:00 | TrangThai → QuaHan, gửi email |
| TC-26 | UC-11 | FR-18 | Trưởng TV đăng nhập | tháng 9/2026 | Hiển thị bảng + biểu đồ |
| TC-27 | UC-07 | BR-10, BR-11, FR-10 | Trả trễ | tre 3 ngày, 2 cuốn | Phạt = 5.000 × 3 × 2 = 30.000đ |
| TC-28 | UC-13 | BR-12, FR-11 | Công nợ 95.000đ, phạt mới 5.000đ | — | TK → Khoa |
| TC-29 | UC-13 | BR-12, FR-11 | Công nợ 99.999đ | không phát sinh thêm | TK vẫn HoatDong |
| TC-30 | UC-08 | BR-13, FR-11 | Công nợ 100.000đ | xin mở khoá | Từ chối, yêu cầu đóng phạt |
| TC-31 | UC-13 | BR-16, FR-03 | Thẻ thư viện hết hạn hôm nay | the.ngayHetHan = today | Từ chối mượn/gia hạn |
| TC-32 | UC-13 | BR-02, FR-04 | GV đang giữ 8 cuốn | xin cuốn thứ 9 | Từ chối |
| TC-33 | UC-09 | FR-16 | Thêm đầu sách | isbn trùng bản ghi cũ | Cảnh báo, không tạo trùng |
| TC-34 | UC-09 | FR-16 | Xoá đầu sách có bản sao DangMuon | — | Từ chối xoá |
| TC-35 | UC-13 | BR-16, FR-03 | SV đang giữ sách quá hạn | — | Từ chối mượn mới |
| TC-36 | UC-02 | FR-20 | Tìm nâng cao | namXB=2023, NXB="Trẻ" | Trả danh sách lọc đúng |
| TC-37 | UC-10 | FR-17 | Đăng ký bạn đọc mới | maSV trùng bản ghi cũ | Từ chối |
| TC-38 | UC-03 | FR-21 | Lập phiếu mượn thành công | 1 cuốn GiaoTrinh | Xuất file PDF phiếu mượn |
| TC-39 | UC-05 | BR-07, FR-08 | Còn đúng 2 ngày trước hạn | ngayDenHan - today = 2 | Cho phép gia hạn |
| TC-40 | UC-05 | BR-06, FR-07 | Đủ mọi điều kiện | soLanGiaHan=1, biKhoaMuon=false, còn 5 ngày | Gia hạn thành công (ngày đến hạn +7) |
| TC-41 | UC-14 | FR-09 | Trả sách | mã bản sao đang DangMuon | TrangThai → CoSan |
| TC-42 | UC-06 | BR-23, FR-13 | Bạn đọc bị khoá | trangThaiTK=Khoa | Từ chối đặt trước |
| TC-43 | UC-01 | FR-01 | Đăng nhập + mượn sách | — | Có dòng log trong bảng nhat_ky |
| TC-44 | UC-10 | BR-21, FR-17 | Thẻ cấp quá 12 tháng | ngayCap = 2024-10-05, hôm nay 2026-10-05 | Từ chối mượn, yêu cầu gia hạn thẻ |
| TC-45 | UC-09 | BR-22, FR-16 | Nhập kho bản sao mới | maDauSach rút gọn = "LTJ", số thứ tự 12 | Sinh mã LTJ-0012 đúng quy tắc |
| TC-46 | UC-07 | BR-20, FR-22 | Phiếu 1 cuốn giá bìa 120.000đ trả trễ 40 ngày | Phạt trễ = 200.000đ | Chỉ thu 120.000đ (trần BR-20); đền bù mất/hỏng tính riêng, không bị cắt (Q1) |
| TC-47 | UC-06 | BR-19, FR-15 | Bạn đọc đã có 2 phiếu đặt trước chờ | Tạo phiếu đặt trước thứ 3 | Từ chối (tối đa 2 phiếu chờ) |
| TC-48 | UC-05 | BR-06, FR-07 | SV đang giữ 5 cuốn | Xin gia hạn 1 phiếu | Cho phép (hạn mức chỉ chặn mượn mới, Q2) |
| TC-49 | UC-04 | FR-09 | Phiếu 3 cuốn trả 1 lần | Thủ thư chỉ quét 1/3 cuốn | Phiếu giữ TraMotPhan; dòng đã trả có ngayTra |
| TC-50 | UC-04 | BR-14, FR-12 | Trả 1 cuốn trễ 3 ngày + 1 cuốn mất | — | 2 phiếu phạt độc lập cho cùng phiếu (TRE + MAT) |
| TC-51 | UC-07 | BR-10, FR-10 | 2 cuốn, trả lệch ngày (trễ 4 và 2 ngày) | — | Phạt = 5.000 × (4+2) = 30.000đ (tính từng dòng, Q5) |
| TC-52 | UC-04 | BR-14, FR-12 | Mất sách giá bìa 100.000đ | Báo mất | Đền 200.000đ (không bị cắt bởi trần BR-20, Q1) |
| TC-53 | UC-03 | BR-05, FR-06 | Mã tạp chí loại TapChi | Xin mượn về | Từ chối |
| TC-54 | UC-01 | BR-13, FR-11 | biKhoaMuon=true do nợ | Đăng nhập | Thành công (chỉ chặn mượn/đặt trước/gia hạn, Q8) |
| TC-55 | UC-06 | FR-13 | Đã có phiếu đặt trước chờ cho sách X | Đặt trước lại X | Từ chối "đã đặt trước" |
| TC-56 | UC-04 | BR-18, FR-14 | Bản sao đang mượn, hàng đợi ≠ rỗng | Trả sách bình thường | Bản sao → DaDatTruoc; người đầu hàng được giữ 3 ngày |
| TC-57 | UC-11 | FR-23 | Trưởng TV đăng nhập | Xuất báo cáo 9/2026 dạng Excel | File tải về đủ số liệu |
| TC-58 | UC-01 | FR-01 | Đã đăng nhập sai 3 lần liên tiếp | Lần thứ 4 | Tạm khoá 15 phút, hiển thị thông báo |
| TC-59 | UC-03 | BR-21 | Thẻ cấp 05/10/2025 | Hôm nay 05/10/2026 | Cho mượn (thẻ còn hạn) |
| TC-60 | UC-03 | BR-21 | Thẻ cấp 06/10/2024 | Hôm nay 06/10/2026 | Từ chối (vừa hết hạn 12 tháng, TC-44 biên) |
