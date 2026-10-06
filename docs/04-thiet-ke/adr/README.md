# ADR — Quyết định kiến trúc

- **ADR-01:** Dùng PlantUML cho mọi sơ đồ thay vì công cụ vẽ kéo-thả → diff được, review được trong Git.
- **ADR-02:** Tài liệu định dạng Markdown thuần, không cần build site.
- **ADR-03:** Kiểm thử truy vết bằng script `scripts/check.sh` (bash + awk + grep) thay vì phụ thuộc Node toolchain.
- **ADR-04:** CSDL mục tiêu: PostgreSQL; trạng thái bản sao/phiếu dùng CHECK constraint (xem `../erd.puml`).
- **ADR-05:** Kiến trúc 3 lớp (Boundary/Control/Entity) — đạt NFR-06, tách UI khỏi nghiệp vụ để mở rộng (thêm chi nhánh).
- **ADR-06:** Phạt tính theo ngày lịch và theo từng dòng `chi_tiet_phieu_muon` (Q5/BR-11), không phụ thuộc "ngày làm việc" thư viện.
- **ADR-07:** `cong_no` không lưu cứng; tính dẫn xuất từ các phiếu phạt (Q7) để tránh lệch giữa thẻ bạn đọc và phiếu phạt.
- **ADR-08:** Tách `tai_khoan.trang_thai` (HoatDong/VoHieuHoa — chặn đăng nhập) khỏi `ban_doc.bi_khoa_muon` (khoá mượn/đặt trước/gia hạn do nợ) (Q8/BR-13).
- **ADR-09:** Nhắc hạn trả dùng cron job 07:00 mỗi ngày thay vì event-driven để đơn giản hoá triển khai; đổi sang hàng đợi sự kiện khi mở rộng kênh thông báo (SMS/WebSocket).
