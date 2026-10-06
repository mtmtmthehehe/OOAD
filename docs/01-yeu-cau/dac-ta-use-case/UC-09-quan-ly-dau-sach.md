# UC-09 — Quản lý đầu sách & bản sao

- **Mã UC:** UC-09
- **Actor chính:** Thủ thư
- **Actor phụ:** Hệ thống
- **Mô tả:** Thêm/sửa/xoá đầu sách, nhập kho bản sao, cập nhật vị trí giá kệ, ghi nhận mất/hỏng.
- **Tiền điều kiện:** Thủ thư đăng nhập với quyền quản trị kho.
- **Hậu điều kiện thành công:** CSDL cập nhật tương ứng.
- **Hậu điều kiện thất bại:** Không thay đổi dữ liệu.

## Luồng sự kiện chính
1. Thủ thư chọn chức năng thêm/sửa/xoá đầu sách.
2. Hệ thống hiển thị form nhập: tên sách, tác giả, thể loại, NXB, năm XB, ISBN, giá bìa.
3. Thủ thư nhập thông tin và xác nhận.
4. Hệ thống kiểm tra ISBN không trùng.
5. Hệ thống lưu DauSach.
6. Với chức năng nhập kho bản sao: thủ thư nhập số lượng, hệ thống sinh BanSaoSach tương ứng với mã vạch duy nhất.

## Luồng thay thế
- 4a. ISBN trùng: cảnh báo, chuyển sang sửa bản ghi cũ.
- 5a. Xoá đầu sách đang có bản sao "Đang mượn": từ chối xoá.

## Tần suất: ~20 lượt/ngày.
