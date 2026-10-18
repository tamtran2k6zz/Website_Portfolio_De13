# Kết quả triển khai thực tế Đề 13

Ngày 18/10/2026, Asia/Saigon. Sinh viên Trần Đặng Công Tâm, DTC245220005, ATTT K23A. Giảng viên Nguyễn Anh Chuyên.

Tài liệu này cập nhật trạng thái sau bản kiểm tra ban đầu `KIEM_TRA_DE13.md`; các kết luận chưa triển khai trong bản cũ là lịch sử trước khi chạy hệ thống.

## Môi trường và truy cập

- Docker Desktop Engine Linux 29.8.2, Compose 5.6.0, context desktop-linux.
- Portfolio: https://localhost:8443 (certificate tự ký); HTTP http://localhost:8080 chuyển hướng HTTPS.
- Admin: https://localhost:8443/login. phpMyAdmin: http://localhost:8081.
- Prometheus: http://localhost:9090/targets. Grafana: http://localhost:3001.
- Grafana dùng 3001 vì 3000 đang được project khác sử dụng. Không dừng hay sửa project khác.
- Mật khẩu admin/Grafana/DB xem riêng trong `.env`, không đưa vào báo cáo hoặc Git.

## Kết quả

| Hạng mục | Minh chứng |
|---|---|
| Website, admin và MySQL | App/MySQL healthy; tạo/sửa dự án lưu vào MySQL; bản ghi CRUD tạm được tạo/xóa thành công; health trả UP/CONNECTED |
| phpMyAdmin | Đăng nhập portfolio_app; hiển thị 5 bảng profiles/projects/sessions/skills/users |
| Nginx | nginx -t qua; HTTPS với RSA 3072/SHA256, SAN localhost/127.0.0.1, 30 ngày; security headers không lặp sau sửa proxy_hide_header |
| Xác thực và CSRF | Admin ẩn danh 403; POST thiếu CSRF 403; cookie Secure/HttpOnly/SameSite Lax; smoke HTTP và HTTPS với CA cục bộ PASS |
| Monitoring | 4 targets UP; nginx_up=1; mysql_up=1; 15 container RAM series trên engine, gồm cả project khác; dashboard có dữ liệu |
| Logging | 3 query đều success: nginx access, HTTP status >=400, login_failed; lần API lấy mẫu trả 10/8/1 dòng (limit 10) |
| Hardening | App UID 1000, read-only rootfs, cap_drop ALL, no-new-privileges; database Internal=true; MySQL không publish ports; app chỉ CRUD trên portfolio.* |
| Backup/restore | portfolio-20261018-154457.sql phục hồi vào portfolio_restore_test; 7 dự án, 8 kỹ năng; checksum profiles/projects/skills/users khớp |
| Tests | 7/7 unit/HTTP tests qua; syntax checks qua; npm audit 0 vulnerabilities tại lần kiểm tra |

Ảnh thật ở `docs/evidence`; snapshot kết quả ở `runtime-checks.json`, `tls-checks.json`. Không đưa dump SQL hoặc secret vào Git.

## Commit mốc

1. `d91ec31`: app/admin + MySQL + phpMyAdmin + Nginx/hardening.
2. `906690e`: Prometheus/Grafana và exporters.
3. `b83279e`: Loki/Promtail.

Các commit bổ sung ghi sửa lỗi thực nghiệm và minh chứng. Repository đã push: https://github.com/tamtran2k6zz/Website_Portfolio_De13.

## Vận hành với TLS đang bật

Giữ đủ bốn file cho mọi lệnh thay đổi cấu hình:

```bash
docker compose -f compose.yaml -f compose.monitoring.yaml -f compose.logging.yaml -f compose.tls.yaml ps -a
python scripts/smoke.py --base https://127.0.0.1:8443 --ca-file certs/server.crt
```

Certificate lần này tạo bằng thư viện cryptography cục bộ trên Windows vì không có OpenSSL CLI trên PATH. `scripts/tls.sh` cung cấp cách tạo tương đương bằng OpenSSL trên Linux. Không chạy setup.py lại khi `.env` đã có. Không dùng down -v để restart.

## Giới hạn

Chưa kiểm thử tải kéo dài, chưa quét CVE image, chưa có alert delivery, log rotation hay MFA. Chứng chỉ tự ký phục vụ demo. Promtail EOL từ 02/03/2026, giữ theo yêu cầu đề; cần chuyển client được hỗ trợ khi vận hành dài hạn. cAdvisor privileged và init root là ngoại lệ cần giải thích. Email profile vẫn là student@example.com, cần thay khi có email cá nhân muốn công khai.
