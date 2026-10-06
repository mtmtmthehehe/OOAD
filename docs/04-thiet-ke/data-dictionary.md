# Data Dictionary — CSDL Quản lý Thư viện

## tai_khoan
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_tk | VARCHAR(20) | PK | Mã tài khoản |
| ten_dang_nhap | VARCHAR(50) | UNIQUE, NOT NULL | Tên đăng nhập |
| mat_khau_hash | VARCHAR(255) | NOT NULL | Mật khẩu đã băm (bcrypt) |
| vai_tro | VARCHAR(20) | CHECK IN (BanDoc, ThuThu, TruongThuVien, HeThong) | Vai trò (UC-01) |
| ma_ban_doc | VARCHAR(20) | FK → ban_doc, NULL | Đúng một trong ma_ban_doc/ma_thu_thu khác NULL |
| ma_thu_thu | VARCHAR(20) | FK → thu_thu, NULL | Tham chiếu thủ thư tương ứng |
| trang_thai | VARCHAR(20) | DEFAULT HoatDong, CHECK IN (HoatDong, VoHieuHoa) | VoHieuHoa chặn đăng nhập (Q8) |

## nhat_ky
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_log | BIGINT | PK | Mã log |
| ma_tk | VARCHAR(20) | FK → tai_khoan | Tài khoản thao tác |
| hanh_dong | VARCHAR(100) | NOT NULL | Tên hành động (mượn/trả/đăng nhập…) |
| doi_tuong | VARCHAR(50) | | Đối tượng tác động |
| thoi_diem | TIMESTAMP | NOT NULL, DEFAULT now() | Thời điểm |
| chi_tiet | TEXT | | Mô tả chi tiết |

## thu_thu
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_thu_thu | VARCHAR(20) | PK | Mã thủ thư |
| ho_ten | VARCHAR(100) | NOT NULL | Họ tên |
| email | VARCHAR(100) | | Email liên hệ |

## dau_sach
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_dau_sach | VARCHAR(20) | PK | Mã đầu sách |
| ten_sach | VARCHAR(255) | NOT NULL | Tên sách |
| isbn | VARCHAR(20) | UNIQUE, NOT NULL | Mã ISBN |
| nam_xuat_ban | INT | | Năm xuất bản |
| gia_bia | DECIMAL(12,2) | NOT NULL | Giá bìa |
| loai_tai_lieu | VARCHAR(20) | CHECK IN (GiaoTrinh, ThamKhao, TapChi) | Loại tài liệu (BR-05) |
| ma_the_loai | VARCHAR(10) | FK → the_loai, NOT NULL | Thể loại |
| ma_nxb | VARCHAR(10) | FK → nha_xuat_ban, NOT NULL | Nhà xuất bản |

## ban_sao_sach
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_ban_sao | VARCHAR(20) | PK | Mã bản sao (mẫu `<XXX>-<dddd>`, BR-22) |
| ma_dau_sach | VARCHAR(20) | FK → dau_sach, NOT NULL | Đầu sách |
| vi_tri_ke | VARCHAR(50) | | Vị trí giá/kệ |
| trang_thai | VARCHAR(20) | CHECK IN (CoSan, DangMuon, DaDatTruoc, Mat, HuHong) | Trạng thái |

## ban_doc
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_ban_doc | VARCHAR(20) | PK | Mã bạn đọc |
| ho_ten | VARCHAR(100) | NOT NULL | Họ tên |
| email | VARCHAR(100) | NOT NULL | Email nhận nhắc hạn (F1) |
| loai | VARCHAR(10) | CHECK IN (SV, GV) | Loại bạn đọc |
| bi_khoa_muon | BOOLEAN | DEFAULT false | Khoá mượn/gia hạn/đặt trước do nợ ≥ 100.000đ (BR-12/13) |

## the_thu_vien
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_the | VARCHAR(20) | PK | Mã thẻ |
| ma_ban_doc | VARCHAR(20) | FK, UNIQUE, NOT NULL | Bạn đọc sở hữu |
| ngay_cap | DATE | | Ngày cấp |
| ngay_het_han | DATE | | = ngay_cap + 12 tháng (BR-21) |
| trang_thai | VARCHAR(20) | DEFAULT HieuLuc, CHECK IN (HieuLuc, HetHan, ThuHoi) | HieuLuc/HetHan/ThuHoi |

## phieu_muon
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_phieu | VARCHAR(20) | PK | Mã phiếu mượn |
| ma_ban_doc | VARCHAR(20) | FK, NOT NULL | Bạn đọc mượn |
| ma_thu_thu | VARCHAR(20) | FK, NOT NULL | Thủ thư lập phiếu |
| ngay_muon | DATE | NOT NULL | Ngày mượn |
| ngay_den_han | DATE | NOT NULL, >= ngay_muon | Hạn = ngày mượn + (SV 14 / GV 30); cập nhật khi gia hạn |
| trang_thai | VARCHAR(20) | CHECK IN (DangMuon, QuaHan, TraMotPhan, DaTra, DaTraTre, MatHuHong) | Trạng thái |
| so_lan_gia_han | INT | DEFAULT 0, CHECK ≤ 2 | Số lần đã gia hạn (BR-06) |

## chi_tiet_phieu_muon
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_ct | VARCHAR(20) | PK | Mã chi tiết |
| ma_phieu | VARCHAR(20) | FK, NOT NULL | Phiếu mượn |
| ma_ban_sao | VARCHAR(20) | FK, NOT NULL | Bản sao |
| ngay_tra | DATE | | Ngày trả (NULL = chưa trả) |

## phieu_phat
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_phieu_phat | VARCHAR(20) | PK | Mã phiếu phạt |
| ma_ct | VARCHAR(20) | FK, NOT NULL | Chi tiết mượn (1 chi tiết có thể có nhiều phiếu: vừa trễ vừa mất) |
| ma_ban_doc | VARCHAR(20) | FK, NOT NULL | Bạn đọc bị phạt |
| loai_phat | VARCHAR(10) | CHECK IN (TRE, MAT, HONG) | Loại phạt (BR-10, BR-14, BR-15) |
| so_ngay_tre | INT | | Số ngày trễ (0 nếu MAT/HONG) |
| so_tien | DECIMAL(12,2) | NOT NULL | Tiền phạt |
| so_tien_da_thu | DECIMAL(12,2) | DEFAULT 0, CHECK <= so_tien | Đã thu (Q6) = Σ `thanh_toan_phat.so_tien` của phiếu, cập nhật cùng giao dịch |
| trang_thai | VARCHAR(20) | DEFAULT ChuaThanhToan, CHECK IN (ChuaThanhToan, ThanhToanMotPhan, DaThanhToan) | Trạng thái |
| ngay_thanh_toan | DATE | | Ngày thanh toán |

## thanh_toan_phat
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_tt | VARCHAR(20) | PK | Mã lần thanh toán |
| ma_phieu_phat | VARCHAR(20) | FK, NOT NULL | Phiếu phạt được thu |
| ma_thu_thu | VARCHAR(20) | FK, NOT NULL | Thủ thư thu tiền |
| so_tien | DECIMAL(12,2) | NOT NULL, CHECK > 0 | Số tiền thu lần này |
| thoi_diem | TIMESTAMP | NOT NULL | Thời điểm thu (phục vụ lịch sử và biên lai, UC-08) |

## phieu_dat_truoc
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_phieu_dt | VARCHAR(20) | PK | Mã phiếu đặt trước |
| ma_ban_doc | VARCHAR(20) | FK, NOT NULL | Bạn đọc đặt |
| ma_dau_sach | VARCHAR(20) | FK, NOT NULL | Đầu sách |
| ma_ban_sao | VARCHAR(20) | FK, NULLABLE | Bản sao được giữ khi đến lượt |
| ngay_dat | DATE | | Ngày đặt |
| vi_tri_hang | INT | | Vị trí hàng đợi (BR-17) |
| han_nhan_sach | DATE | | Hạn nhận = ngày đến lượt + 3 ngày (BR-18) |
| trang_thai | VARCHAR(20) | DEFAULT DangCho, CHECK IN (DangCho, SanSangNhan, DaNhan, DaHuy) | Trạng thái |

## tac_gia
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_tac_gia | VARCHAR(20) | PK | Mã tác giả |
| ho_ten | VARCHAR(100) | NOT NULL | Họ tên |

## the_loai
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_the_loai | VARCHAR(10) | PK | Mã thể loại |
| ten_the_loai | VARCHAR(50) | NOT NULL | Tên thể loại |

## nha_xuat_ban
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_nxb | VARCHAR(10) | PK | Mã NXB |
| ten_nxb | VARCHAR(100) | NOT NULL | Tên NXB |

## dau_sach_tac_gia
| Cột | Kiểu | Ràng buộc | Mô tả |
|-----|------|-----------|-------|
| ma_dau_sach | VARCHAR(20) | FK, PK | Đầu sách |
| ma_tac_gia | VARCHAR(20) | FK, PK | Tác giả (nhiều–nhiều) |

## View v_cong_no (Q7)
cong_no của bạn đọc = Σ(so_tien − so_tien_da_thu) của các phiếu phạt chưa `DaThanhToan`.

## Chỉ mục (NFR-01, NFR-05, NFR-08)
| Chỉ mục | Bảng (cột) | Mục đích |
|---------|-----------|----------|
| ix_dau_sach_fts | dau_sach — GIN(to_tsvector('simple', ten_sach)) | Tra cứu theo tên ≤ ngưỡng NFR-01 |
| ix_dau_sach_isbn | dau_sach (isbn) UNIQUE | Chống trùng ISBN (UC-09), tra cứu theo ISBN |
| ix_ban_sao_dau_sach | ban_sao_sach (ma_dau_sach, trang_thai) | Đếm bản sao "Có sẵn" khi mượn/đặt trước |
| ix_pm_ban_doc | phieu_muon (ma_ban_doc, trang_thai) | Kiểm tra phiếu quá hạn/hạn mức (UC-13), NFR-05 |
| ix_pm_den_han | phieu_muon (ngay_den_han) WHERE trang_thai IN ('DangMuon','TraMotPhan') | Cron nhắc hạn (UC-12, NFR-08) |
| ix_pp_ban_doc | phieu_phat (ma_ban_doc, trang_thai) | View v_cong_no |
| ix_dt_hang | phieu_dat_truoc (ma_dau_sach, trang_thai, vi_tri_hang) | Hàng đợi đặt trước (BR-17) |

