# Báo cáo tổng hợp — Đồ án OOAD DT01

## 1. Mục tiêu
Tin học hoá quy trình mượn – trả – gia hạn – phạt của thư viện 2 tầng, ~18.000 đầu sách, thay thế sổ giấy và Excel.

## 2. Phạm vi
Bao gồm: quản lý đầu sách/bản sao, bạn đọc/thẻ, mượn/trả/gia hạn, đặt trước, phạt và thanh toán, thống kê báo cáo, nhắc hạn tự động. Ngoài phạm vi: mua sắm, kế toán chi tiết, liên thông liên thư viện.

## 3. Phương pháp thực hiện
Phân tích hướng đối tượng theo 4 giai đoạn: khảo sát → use case → phân tích thiết kế → hoàn chỉnh. Công cụ: PlantUML cho biểu đồ, Markdown cho tài liệu.

## 4. Kết quả đạt được
- 23 luật nghiệp vụ (BR-01…BR-23) — quy-tac-nghiep-vu.md
- 23 yêu cầu chức năng (FR-01…FR-23) — yeu-cau-chuc-nang.md; 9 yêu cầu phi chức năng (NFR-01…NFR-09) — yeu-cau-phi-chuc-nang.md
- Danh sách 4 mâu thuẫn khảo sát và 9 quyết định thiết kế (Q1–Q9) — bang-mau-thuan.md
- 14 Use Case (UC-01…UC-14), sơ đồ use case có include/extend — mo-hinh-use-case.md, so-do-use-case.puml
- 14 đặc tả UC chi tiết trong `docs/01-yeu-cau/dac-ta-use-case/`
- Ma trận truy vết BR–FR–UC–Lớp — ma-tran-truy-vet.md
- Domain model; class diagram 14 lớp Entity + 9 lớp Boundary/Control trong danh-sach-lop.md (CLS-01…CLS-23)
- 4 sequence diagram cho UC lõi (Mượn, Trả, Gia hạn, Đặt trước)
- 2 state diagram: BanSaoSach, PhieuMuon
- ERD 15 bảng + data dictionary
- 11 màn hình wireframe
- 60 test case (TC-01…TC-60) — ca-kiem-thu.md, phủ mọi BR và mọi UC

## 5. Hạn chế
- Số liệu khảo sát mang tính giả định; chưa khảo sát bạn đọc trực tiếp. Kế hoạch khắc phục: phỏng vấn thêm 10–15 bạn đọc và 2 thủ thư trước khi chốt bản chính thức (dự kiến tháng 11/2026).
- Chưa có cài đặt chương trình thật (chỉ dừng ở thiết kế).

## 6. Hướng phát triển
- Xây dựng prototype web (Spring Boot / React).
- Tích hợp thẻ RFID, gửi email/SMS nhắc hạn.
- Mở rộng liên thông với thư viện các khoa.

## Mục lục tài liệu
Xem bản đồ tài liệu đầy đủ tại [docs/README.md](README.md).
