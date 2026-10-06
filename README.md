# Hệ thống Quản lý Thư viện Trường Đại học (DT01)

Bộ yêu cầu, phân tích và thiết kế cho hệ thống quản lý thư viện 2 tầng, ~18.000 đầu sách. Repository chứa **tài liệu thiết kế và công cụ kiểm tra tài liệu**, chưa chứa ứng dụng vận hành.

- [Bản đồ tài liệu](docs/README.md)
- [Tổng quan](docs/00-tong-quan.md)
- [Quy tắc nghiệp vụ](docs/02-nghiep-vu/quy-tac-nghiep-vu.md)
- [Mô hình Use Case](docs/01-yeu-cau/mo-hinh-use-case.md)
- [Thiết kế lớp & CSDL](docs/04-thiet-ke/)
- [Ma trận truy vết](docs/06-truy-vet/ma-tran-truy-vet.md)
- [Hướng dẫn bàn giao](docs/07-ban-giao/huong-dan-thi-cong.md)

## Cấu trúc repo

```
docs/
  00-tong-quan.md
  01-yeu-cau/        # FR, NFR, mô hình UC, đặc tả UC
  02-nghiep-vu/      # BR, chính sách, khảo sát
  03-phan-tich/      # domain model, state machine
  04-thiet-ke/       # class diagram, sequence, ERD, CSDL, màn hình, ADR
  05-ke-hoach/       # ca kiểm thử, nhật ký nhóm
  06-truy-vet/       # ma trận truy vết
  07-ban-giao/       # hướng dẫn thi công, kết quả kiểm chứng
scripts/             # plantuml.jar, render-all.sh, check.sh
```

## Kiểm tra tại máy

```bash
bash scripts/check.sh        # truy vết BR/FR/UC/TC + cú pháp PlantUML
bash scripts/render-all.sh   # render lại toàn bộ .png từ .puml
```

`check.sh` không phải kiểm thử ứng dụng thật; nó chỉ bảo đảm tài liệu nhất quán (mọi BR/UC có TC, mọi FR xuất hiện trong ma trận, sơ đồ hợp lệ).
