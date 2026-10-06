# Quản lý Thư viện Trường Đại học (DT01) — Bản đồ tài liệu

Tài liệu phân tích – thiết kế cho đồ án môn OOAD. Repository chứa **tài liệu thiết kế và công cụ kiểm tra tài liệu**, chưa chứa ứng dụng vận hành.

- [Tổng quan](00-tong-quan.md)
- Chủ đầu tư: Trường Đại học — Phòng Quản lý Thư viện
- Quy mô: 2 tầng, ~18.000 đầu sách, mượn – trả – gia hạn – phạt

## Bản đồ tài liệu

| # | Tài liệu | Nội dung |
|---|----------|----------|
| 00 | [Tổng quan](00-tong-quan.md) | Mục tiêu, phạm vi, kết quả, số liệu |
| 01 | [Yêu cầu chức năng](01-yeu-cau/yeu-cau-chuc-nang.md) | 23 FR |
| 01 | [Yêu cầu phi chức năng](01-yeu-cau/yeu-cau-phi-chuc-nang.md) | 9 NFR |
| 01 | [Mô hình Use Case](01-yeu-cau/mo-hinh-use-case.md) + [đặc tả UC](01-yeu-cau/dac-ta-use-case/) | 14 UC |
| 02 | [Quy tắc nghiệp vụ](02-nghiep-vu/quy-tac-nghiep-vu.md) | 23 BR — nguồn chân lý |
| 02 | [Chính sách phạt/gia hạn/đặt trước](02-nghiep-vu/chinh-sach-phat-gia-han-dat-truoc.md) | Tóm tắt quyết định |
| 02 | [Bảng mâu thuẫn](02-nghiep-vu/bang-mau-thuan.md) · [Biên bản phỏng vấn](02-nghiep-vu/bien-ban-phong-van.md) | Khảo sát |
| 03 | [Domain model](03-phan-tich/domain-model.puml) · [State máy](03-phan-tich/bieu-do-trang-thai/) | Phân tích |
| 04 | [Class diagram](04-thiet-ke/class-diagram.puml) · [Sequence](04-thiet-ke/bieu-do-tuan-tu/) · [ERD](04-thiet-ke/erd.puml) · [Data dictionary](04-thiet-ke/data-dictionary.md) · [Màn hình](04-thiet-ke/thiet-ke-man-hinh.md) · [ADR](04-thiet-ke/adr/README.md) | Thiết kế |
| 05 | [Ca kiểm thử](05-ke-hoach/ca-kiem-thu.md) · [Nhật ký nhóm](05-ke-hoach/nhat-ky-nhom.md) | Kế hoạch |
| 06 | [Ma trận truy vết](06-truy-vet/ma-tran-truy-vet.md) | BR→FR→UC→CLS→TC |
| 07 | [Hướng dẫn thi công](07-ban-giao/huong-dan-thi-cong.md) · [Kết quả kiểm chứng](07-ban-giao/ket-qua-kiem-chung.md) | Bàn giao |

## Quy ước chung
1. Mã định danh (BR-, FR-, NFR-, UC-, CLS-, TC-, ADR-) duy nhất toàn repo, không đổi số sau khi tham chiếu.
2. Sơ đồ bằng PlantUML (`.puml`) cạnh file render `.png`.
3. Số liệu nghiệp vụ chỉ định nghĩa ở `02-nghiep-vu/quy-tac-nghiep-vu.md`; nơi khác tham chiếu mã BR.
4. Kiểm chứng: `bash scripts/check.sh`.
