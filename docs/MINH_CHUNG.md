# Minh chứng và kiểm thử

Đặt ảnh thực tế vào `docs/evidence/`. Không có screenshot vận hành được tạo sẵn trong bộ này. Bảng dưới đây là kế hoạch chụp, chưa phải kết quả.

| Mã | Ảnh đề xuất | Nội dung cần thấy | Tiêu chí |
|---|---|---|---|
| E01 | 01-compose-stage1.png | Services và trạng thái | Tổng thể |
| E02 | 02-portfolio.png | Website có dữ liệu thật từ DB | App |
| E03 | 03-admin.png | CRUD nội dung | App |
| E04 | 04-phpmyadmin.png | Dòng dữ liệu vừa thay đổi | DB |
| E05 | 05-nginx-headers.png | Security headers hoặc HTTPS | Nginx |
| E06 | 06-prometheus-targets.png | 4 scrape targets UP | Monitoring |
| E07 | 07-container-metrics.png | CPU/RAM/network theo container | Monitoring |
| E08 | 08-web-db-metrics.png | Nginx/MySQL metrics thật | Monitoring |
| E09 | 09-loki-access.png | Query access log và kết quả | Logging |
| E10 | 10-loki-http-errors.png | Query status>=400 và event 404 | Logging |
| E11 | 11-loki-login-failed.png | Query login_failed và event | Logging/ATTT |
| E12 | 12-nonroot.png | UID app và Nginx | Hardening |
| E13 | 13-network.png | DB internal, không Nginx/host mapping | Hardening |
| E14 | 14-db-grants.png | Quyền user ứng dụng | Hardening |
| E15 | 15-security-tests.png | CSRF/access control/rate limit | Hardening |
| E16 | 16-backup-restore.png | DB thử và đối chiếu dữ liệu | Vận hành |
| E17 | 17-github-commits.png | Repo, 3 commit có ý nghĩa | GitHub |

Ghi chú thích mỗi ảnh: thời điểm, thao tác, điều chứng minh. Che password, cookie, session IDs và dữ liệu riêng tư. Tránh chỉ chụp cấu hình mà không có kết quả runtime.

| Test | Thao tác | Expected | Actual | Kết quả |
|---|---|---|---|---|
| TC01 | GET / qua Nginx | 200, dữ liệu portfolio | [Điền] | [Điền] |
| TC02 | Đăng nhập đúng | Vào admin | [Điền] | [Điền] |
| TC03 | Thêm/sửa/xóa dự án | DB và UI thay đổi đúng | [Điền] | [Điền] |
| TC04 | Chưa login mở admin | 403 | [Điền] | [Điền] |
| TC05 | Sai password 6 lần với token | 5 lỗi 401 rồi 429 | [Điền] | [Điền] |
| TC06 | POST thiếu CSRF | 403 | [Điền] | [Điền] |
| TC07 | Nội dung chứa script | Hiển thị text, không thực thi | [Điền] | [Điền] |
| TC08 | Link javascript qua POST hợp lệ | 400 | [Điền] | [Điền] |
| TC09 | Stop/start stack | Dữ liệu vẫn tồn tại | [Điền] | [Điền] |
| TC10 | Metrics container/web/DB | Series và panel có dữ liệu | [Điền] | [Điền] |
| TC11 | Tạo 404, query Loki | Tìm đúng request/status | [Điền] | [Điền] |
| TC12 | Backup/restore thử | Nội dung khôi phục đúng | [Điền] | [Điền] |
| TC13 | Đổi password và logout | Sessions cũ không vào admin | [Điền] | [Điền] |
| TC14 | HTTPS tùy chọn | Kết nối TLS, Secure cookie | [Điền] | [Điền] |

