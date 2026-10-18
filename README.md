# Đề 13: Portfolio có admin - Docker Compose

Sinh viên: **Trần Đặng Công Tâm — DTC245220005 — ATTT K23A**. Giảng viên: **Nguyễn Anh Chuyên**.

Repository: https://github.com/tamtran2k6zz/Website_Portfolio_De13

Đã chạy thực nghiệm ngày 18/10/2026 trên Docker Desktop Linux: app/MySQL healthy, admin CRUD, phpMyAdmin, Nginx HTTP/HTTPS, 4 Prometheus targets UP, dashboard Grafana, 3 LogQL queries có dữ liệu và backup/restore thử. Xem [kết quả nghiệm thu](docs/KET_QUA_TRIEN_KHAI.md) và [ảnh minh chứng](docs/evidence/).

Ứng dụng thật dùng Node.js/Express/EJS + MySQL, không dùng dữ liệu mock khi triển khai. Mục tiêu là hoàn thành các yêu cầu triển khai của môn Triển khai và Quản trị Hệ thống Phần mềm.

**Bắt đầu:** đọc `docs/HUONG_DAN_A_Z.md`. **Viết báo cáo:** dùng `docs/KHUNG_BAO_CAO.md` và `docs/MINH_CHUNG.md`. Đọc phạm vi kiểm tra ở `docs/VALIDATION.md` trước khi tuyên bố hệ thống đã chạy.

## Chuẩn bị

- Docker Engine và Docker Compose v2 chạy Linux containers; nên dùng Ubuntu Linux để thu container metrics ổn định.
- Windows: Docker Desktop với WSL2 và tích hợp Ubuntu. Đọc mục giới hạn cAdvisor trong hướng dẫn.
- Python 3, Git, Internet trong lần đầu pull/build; không cần Node.js trên host để chạy Docker.
- Mức tài nguyên khởi đầu đề xuất: 4 CPU, 6-8 GB RAM cấp cho môi trường Docker; điều chỉnh theo máy thực tế.

```bash
python3 scripts/setup.py
python3 scripts/compose.py 1 up -d --build
python3 scripts/compose.py 1 ps -a
python3 scripts/smoke.py
```

Mở `http://localhost:8080`, admin tại `/login`. Tài khoản ứng dụng: `ADMIN_USERNAME`, mật khẩu: `ADMIN_INITIAL_PASSWORD` trong `.env`. phpMyAdmin ở `http://localhost:8081`, đăng nhập bằng `portfolio_app` và `APP_DB_PASSWORD`. Không đưa `.env` lên Git.

## Ba giai đoạn

| Giai đoạn | Lệnh | Thành phần |
|---|---|---|
| 1 | `python3 scripts/compose.py 1 up -d --build` | App, MySQL, phpMyAdmin, Nginx |
| 2 | `python3 scripts/compose.py 2 up -d --build` | Thêm exporters, Prometheus, Grafana |
| 3 | `python3 scripts/compose.py 3 up -d --build` | Thêm Loki, Promtail, datasource Loki |

Sau mỗi giai đoạn: `python3 scripts/compose.py N ps -a` và `python3 scripts/compose.py N logs --tail=80`. Thay N bằng 1, 2 hoặc 3. Dùng đúng giai đoạn cao nhất đã triển khai khi stop/start.

Grafana: `http://localhost:3001`, user `admin`, mật khẩu `GRAFANA_ADMIN_PASSWORD`. Dashboard tự provision trong folder `De 13`. Prometheus: `http://localhost:9090/targets`.

```bash
python3 scripts/traffic.py
```

LogQL trong Grafana > Explore > Loki:

```logql
{job="nginx"}
{job="nginx"} | json | status >= 400
{job="app"} | json | event="login_failed"
```

## Backup và vận hành

```bash
python3 scripts/backup.py
python3 scripts/restore-test.py backups/TEN_FILE_VUA_TAO.sql
python3 scripts/compose.py 3 stop
python3 scripts/compose.py 3 start
```

Restore thử tạo DB `portfolio_restore_test` riêng và từ chối nếu DB đó đã tồn tại. Không xóa volume để xử lý lỗi thông thường. `down -v` xóa dữ liệu.

## HTTPS tùy chọn

```bash
sh scripts/tls.sh
docker compose -f compose.yaml -f compose.monitoring.yaml -f compose.logging.yaml -f compose.tls.yaml up -d --build
```

Mở `https://localhost:8443`. Certificate tự ký chỉ cho demo; trình duyệt cảnh báo do chưa tin CA. Khi dùng TLS, mọi lệnh Compose phục vụ thay đổi cấu hình phải giữ đủ 4 file; wrapper ba giai đoạn không tự thêm file TLS. Xem hướng dẫn chi tiết.

## Kiểm tra mã nguồn

Chỉ khi muốn chạy tests bên ngoài Docker, cài Node >=24:

```bash
cd app
npm ci
npm test
npm run check
npm audit --omit=dev
```

Tests HTTP dùng repository và session store thay thế chỉ trong tests; không xác nhận tích hợp MySQL/container. Kiểm chứng Docker thực tế được ghi riêng trong `docs/KET_QUA_TRIEN_KHAI.md`.

## Giới hạn

- Một tài khoản admin, chưa có hệ thống nhiều vai trò; quản lý kỹ năng bằng thêm/xóa.
- Session lưu MySQL; bộ đếm rate limit lưu RAM và reset khi app restart, phù hợp một instance demo.
- Log tập trung ở phạm vi Nginx access/error và ứng dụng. MySQL được giám sát bằng metrics; chưa thu toàn bộ log mọi container.
- cAdvisor cần quyền host cao để thu metrics; không tuyên bố mọi container đều non-root/hạn chế quyền giống nhau.
- Promtail đã EOL ngày 02/03/2026 nhưng dùng theo PDF; chỉ thay Alloy khi giảng viên đồng ý.
- Image dùng phiên bản cụ thể để tái lập bài; chưa quét CVE của image. Cần đánh giá/cập nhật và kiểm tra lại trước khi dùng ngoài môi trường học tập.
- Chưa có email, upload, MFA, WAF hay tự động gửi cảnh báo ra bên ngoài. Prometheus có alert rules về availability, không phải một SIEM hoàn chỉnh.

## Tài liệu chính thức

- https://docs.docker.com/desktop/features/wsl/
- https://docs.docker.com/compose/how-tos/startup-order/
- https://prometheus.io/docs/guides/cadvisor/
- https://github.com/nginx/nginx-prometheus-exporter
- https://github.com/prometheus/mysqld_exporter
- https://grafana.com/docs/loki/latest/send-data/promtail/
- https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

