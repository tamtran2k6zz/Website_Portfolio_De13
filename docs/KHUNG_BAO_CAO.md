# Khung báo cáo cuối kỳ Đề 13

**Đây là khung điền nội dung, không phải báo cáo kết quả đã hoàn thành.** Thay toàn bộ `[ ... ]` bằng thông tin/kết quả thật. Báo cáo tối thiểu 10 trang theo PDF; nên dành 12-15 trang nội dung nếu đủ minh chứng. Định dạng Word theo mẫu giảng viên, không tự coi số trang Markdown là số trang báo cáo.

## Bìa

[TÊN TRƯỜNG]

[KHOA]

BÁO CÁO CUỐI KỲ

MÔN: TRIỂN KHAI VÀ QUẢN TRỊ HỆ THỐNG PHẦN MỀM

**Đề 13: Triển khai và quản trị website Portfolio cá nhân an toàn bằng Docker Compose, tích hợp giám sát và log tập trung**

- Sinh viên: [Họ tên]
- MSSV: [MSSV]
- Lớp: [Lớp]
- Giảng viên: [Họ tên]
- Thời gian: [Tháng/năm]
- Repository: [URL thực tế]

Sau bìa: mục lục tự động; danh mục hình/bảng nếu cần.

## Chương 1. Giới thiệu (khoảng 1 trang)

### 1.1 Lý do chọn đề tài

Giải thích nhu cầu portfolio có admin; vì sao phù hợp bài triển khai; hướng ATTT tập trung vào xác thực, quyền truy cập, network isolation và log. Không tuyên bố đạt mức bảo mật tuyệt đối.

### 1.2 Mục tiêu

Ứng dụng có DB thật, reverse proxy, monitoring container/web/DB, logging, hardening, GitHub và khả năng demo. Liên hệ rõ từng yêu cầu PDF.

### 1.3 Phạm vi

Một admin, nội dung profile/projects/skills. Chưa có upload, nhiều vai trò, MFA, WAF hoặc SIEM đầy đủ. [Ghi các phần bạn thực sự bổ sung hoặc cắt giảm.]

## Chương 2. Thiết kế hệ thống (khoảng 2 trang)

### 2.1 Môi trường triển khai

| Thuộc tính | Giá trị thật |
|---|---|
| Host OS / WSL | [Điền] |
| CPU/RAM cấp cho Docker | [Điền] |
| Docker Engine/Desktop | [Kết quả docker version] |
| Docker Compose | [Phiên bản] |
| Ngày kiểm tra | [Điền] |

### 2.2 Kiến trúc

Chèn sơ đồ trong hướng dẫn (render thành hình nếu đưa Word). Mô tả request Browser -> Nginx -> App -> MySQL. Giải thích Prometheus scrape exporters và Promtail push logs. **Hình 2.1: Kiến trúc hệ thống [do bạn dựng từ cấu hình thực tế].**

### 2.3 Database

Mô tả 5 bảng và mục đích; không cố tạo quan hệ 1-N nếu schema thực tế không có. Tài khoản ứng dụng và tài khoản exporter tách nhau. **Hình 2.2: Các bảng trong phpMyAdmin.**

### 2.4 Mạng và volume

Mô tả web/database/management/monitoring; ai nối vào mạng nào; cổng host; dữ liệu nào persistent. Nêu DB internal và Nginx không truy cập trực tiếp mạng DB.

## Chương 3. Quản lý source và triển khai cơ bản (khoảng 2 trang)

### 3.1 GitHub

URL repo, cấu trúc source, README, bảng commit hash/ngày/nội dung thực tế. Source mẫu đã được chỉnh sửa/kiểm chứng thế nào. **Hình 3.1: Repository và lịch sử commit.**

### 3.2 Dockerfile và Compose

Giải thích image, build, USER node, healthchecks, dependencies và named volumes. Trích đoạn cấu hình ngắn; không chép toàn bộ YAML để tăng số trang.

### 3.3 App + DB + phpMyAdmin

[Mô tả ca CRUD, dữ liệu trước/sau, kết quả.] **Hình 3.2: Trang portfolio. Hình 3.3: Admin. Hình 3.4: Dữ liệu dự án trong MySQL.**

### 3.4 Nginx

Mô tả proxy_pass, forwarded headers, security headers và access log JSON. Nếu làm HTTPS, mô tả certificate tự ký, thời hạn, cookie Secure và giới hạn trust. **Hình 3.5: Kết quả headers/HTTPS.**

## Chương 4. Giám sát hệ thống (khoảng 2 trang)

### 4.1 Nguồn metrics

| Nguồn | Service được giám sát | Ví dụ metrics |
|---|---|---|
| cAdvisor | Container | CPU, memory, network |
| Nginx Exporter | Nginx | nginx_up, request count, active connections |
| MySQL Exporter | MySQL | mysql_up, threads connected, queries |

### 4.2 Thu thập và dashboard

Scrape interval, targets, datasource, tên dashboard. Chụp targets UP và service metrics bằng 1. **Hình 4.1: Prometheus Targets. Hình 4.2: Container dashboard. Hình 4.3: Nginx/MySQL dashboard.**

### 4.3 Thử nghiệm

[Giờ chạy 30 request, số request trả 200/404, thời gian chờ scrape, panel nào thay đổi.] Diễn giải đúng CPU %, bytes và rate. Nêu giới hạn cAdvisor trên host nếu có. Target UP không thay cho minh chứng metric thật.

## Chương 5. Log tập trung (khoảng 1,5-2 trang)

### 5.1 Luồng log

File log -> Promtail -> Loki -> Grafana. Label jobs, timestamp, positions và retention. Phạm vi Nginx/app, không tự tuyên bố mọi container.

### 5.2 Ba query bắt buộc

| Query | Mục đích | Sự kiện tạo thử | Kết quả |
|---|---|---|---|
| `{job="nginx"}` | Log truy cập | [Request thật] | [Điền] |
| `{job="nginx"} \| json \| status >= 400` | Lỗi HTTP | [URL 404 thật] | [Điền] |
| `{job="app"} \| json \| event="login_failed"` | Sai đăng nhập | [Thời điểm] | [Điền] |

Chèn 3 screenshot có query và kết quả, chú thích rõ thời điểm. Dòng log không chứa mật khẩu hoặc cookie. Nếu viết về Promtail, ghi EOL 02/03/2026 và lý do dùng theo đề.

## Chương 6. Hardening và ATTT (khoảng 2 trang)

| Biện pháp | Cấu hình áp dụng | Kiểm chứng thực tế |
|---|---|---|
| Non-root | App/Nginx/Loki/Promtail | [UID thật] |
| Network isolation | Database internal, DB không publish | [Inspect/ports] |
| DB least privilege | portfolio_app CRUD only | [SHOW GRANTS] |
| Quyền container | Cap drop, no-new-privileges, read-only app | [Cấu hình/inspect] |
| Web protection | Session, CSRF, escape, rate limit | [Kết quả test] |
| Secrets | .gitignore, mật khẩu riêng | [git check-ignore; không chụp giá trị] |

Giải thích cAdvisor privileged và init-log root là ngoại lệ. Quyền exporter đọc rộng theo yêu cầu collector khác quyền app. Trình bày các log auth_denied/csrf_denied/login_rate_limited nếu đã thử. Mật khẩu băm không đồng nghĩa mã hóa có thể giải ngược.

## Chương 7. Kiểm thử, vận hành và kết luận (khoảng 1,5-2 trang)

### 7.1 Bảng kiểm thử

Điền bảng test trong `MINH_CHUNG.md`: expected/actual/pass/fail. Phân biệt tests dùng repository thay thế với kiểm tra MySQL/Docker thực tế.

### 7.2 Backup, restore, restart

Ngày backup, file dump (không đính kèm secrets), DB restore_test, số dòng nguồn/restore và kết quả so sánh. Restart vẫn có dữ liệu. **Hình 7.1: Backup/restore. Hình 7.2: Dữ liệu sau restart.**

### 7.3 Kết luận

[Yêu cầu hoàn thành thực tế, phần chưa làm, lỗi đã xử lý.] Hướng phát triển có thể là MFA, alert delivery, log rotation, Alloy, image CVE scanning. Không viết đã triển khai nếu chỉ là hướng phát triển.

## Tài liệu tham khảo

Đưa PDF môn học và các nguồn chính thức trong README. Ghi ngày truy cập thật. Nếu dùng công cụ hỗ trợ tạo code, khai báo theo yêu cầu học thuật của giảng viên và giải thích phần bạn hiểu/chỉnh sửa/kiểm thử.

## Phụ lục

Lệnh triển khai, LogQL/PromQL, commit hashes, checklist và các trích đoạn cấu hình quan trọng. Không chèn `.env`, mật khẩu, private key hay session IDs.
