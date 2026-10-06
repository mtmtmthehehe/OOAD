# UC-01 — Đăng nhập & phân quyền

- **Mã UC:** UC-01
- **Mã tên:** Đăng nhập & phân quyền
- **Actor chính:** Bạn đọc / Thủ thư / Trưởng thư viện
- **Actor phụ:** Hệ thống
- **Mô tả:** Xác thực thông tin tài khoản và cấp quyền truy cập theo vai trò.
- **Tiền điều kiện:** Người dùng có tài khoản trong hệ thống.
- **Hậu điều kiện (thành công):** Người dùng đăng nhập thành công, được chuyển vào màn hình phù hợp vai trò.
- **Hậu điều kiện (thất bại):** Không thay đổi dữ liệu, hiển thị thông báo lỗi.

## Luồng sự kiện chính
1. Người dùng nhập tên đăng nhập và mật khẩu.
2. Hệ thống kiểm tra thông tin đăng nhập.
3. Hệ thống kiểm tra `tai_khoan.trang_thai`: nếu `VoHieuHoa` → từ chối (bước 3a). Khoá do nợ (`ban_doc.bi_khoa_muon`) KHÔNG chặn đăng nhập (Q8).
4. Hệ thống xác định vai trò và mở giao diện tương ứng.

## Luồng thay thế
- 2a. Sai tên đăng nhập/mật khẩu: hệ thống báo lỗi, cho phép nhập lại tối đa 3 lần.
- 3a. Tài khoản `VoHieuHoa`: từ chối đăng nhập, hiển thị lý do.
- 2b. Sai mật khẩu liên tiếp 3 lần: tạm khoá đăng nhập 15 phút (NFR-09); lần thứ 4 hiển thị "tạm khoá 15 phút".

## Luồng ngoại lệ
- Hệ thống mất kết nối CSDL: hiển thị "Lỗi hệ thống, vui lòng thử lại sau".

## Yêu cầu đặc biệt
- Mật khẩu lưu dạng băm (NFR-03).
- Sai mật khẩu 3 lần → tạm khoá 15 phút (NFR-09).

## Tần suất: ~300 lượt/ngày.
