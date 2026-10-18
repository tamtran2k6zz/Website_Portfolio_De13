# Phạm vi kiểm tra bộ bàn giao

**Cập nhật 18/10/2026:** stack đã được triển khai thực tế trên Docker Desktop của sinh viên. Xem `KET_QUA_TRIEN_KHAI.md` và `evidence/` để biết kết quả mới. Các mục “chưa kiểm tra” bên dưới mô tả môi trường tạo bộ file ban đầu, không phải trạng thái nghiệm thu hiện tại.

## Đã kiểm tra trong môi trường tạo bộ file

- Node.js v24.19.0, npm install và lockfile.
- 7 tests qua: mật khẩu băm/salt; URL/ID validation; bound SQL parameter; HTTP access control/CSRF/headers; CRUD qua repository test và escape XSS; giới hạn đăng nhập sai; validation/logout.
- HTTP tests dùng repository thay thế và MemoryStore chỉ trong tests. Server triển khai dùng repository MySQL và MysqlSessionStore.
- `npm run check` qua; `npm audit --omit=dev` báo **0 vulnerabilities** tại thời điểm kiểm tra cuối sau cập nhật mysql2 và express-rate-limit. Audit không chứng minh không có lỗ hổng ứng dụng hay image.
- 12 file YAML của dự án parse được; dashboard JSON parse được; shell/Python syntax qua; kiểm tra đường dẫn bind mount có sẵn (không tính secrets/certs sinh sau).
- Docker Compose standalone v2.40.3 đã kiểm tra cấu hình stage 1/2/3 và TLS bằng `config --format json`, dùng placeholder secrets trong bộ nhớ. Các cấu hình hợp lệ; kiểm tra merge TLS, database internal, app/MySQL không publish ports. Chưa chạy container.
- Setup secrets được chạy ở thư mục thử tách biệt: mật khẩu được tạo đồng bộ, không in secret, từ chối ghi đè.
- Registry xác nhận manifest Node và 10 image/tag trên Docker Hub trong Compose tồn tại. Điều này không phải kết quả build/run hay image CVE scan.

## Chưa kiểm tra tại đây

Môi trường tạo bộ file không có Docker daemon. Vì vậy chưa chạy Docker build, MySQL init, Nginx runtime, exporter scrapes, Grafana provisioning, Loki/Promtail ingestion, HTTPS, backup/restore với DB thật hay cAdvisor trên host của bạn.

Các bước trên phải được thực hiện và ghi actual results trên máy bạn theo `HUONG_DAN_A_Z.md`. Nếu có lỗi, dùng troubleshooting và ghi thay đổi cấu hình thực tế. Không ghi báo cáo rằng toàn stack đã chạy dựa trên kết quả tests ở đây.

## Mục tiêu nghiệm thu trên máy bạn

1. Compose config hợp lệ ở stage 1/2/3 (và TLS nếu dùng).
2. App/DB healthy, admin CRUD lưu vào MySQL, phpMyAdmin đối chiếu đúng.
3. Website qua Nginx, headers/HTTPS hoạt động.
4. Targets UP + mysql_up/nginx_up=1 + container metrics thật.
5. Dashboard có dữ liệu; 3 LogQL queries trả đúng event tạo thử.
6. Non-root/network/DB permissions được kiểm chứng, secrets không vào Git.
7. Restart bảo toàn dữ liệu, backup/restore thử đúng.
8. README đủ để người khác tái lập; báo cáo đủ trang và screenshot thật.
