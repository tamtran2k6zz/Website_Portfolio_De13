# Kiểm tra project theo Đề 13

Ngày kiểm tra: 18/10/2026 (Asia/Saigon).

## Kết luận

Mã nguồn và cấu hình bao phủ các thành phần chính của đề. **Chưa đủ minh chứng để kết luận bài đã hoàn thành hoặc sẵn sàng nộp.** Repository GitHub còn trống; thư mục local không có `.git`; chưa có báo cáo hoàn chỉnh và ảnh vận hành. Không chấm điểm giả định từ cấu hình.

Phạm vi: đọc mã ứng dụng, schema, Compose, Nginx, Prometheus, Grafana, Loki/Promtail và tài liệu; chạy tests và kiểm tra cấu hình. Chưa build/chạy stack portfolio, chưa kiểm tra giao diện bằng trình duyệt, chưa chạy integration với MySQL thật. Giả định hệ thống demo một admin, một instance app.

## Đối chiếu tiêu chí

| Tiêu chí | Có trong project | Kết luận và phần còn thiếu |
|---|---|---|
| GitHub + README + ít nhất 3 commit có ý nghĩa (1,5 điểm) | README, hướng dẫn A–Z, cấu hình được chia thành 3 giai đoạn | **Chưa đạt minh chứng.** `git status`, `git remote`, `git log` đều báo không có repository local. GitHub API trả `409 Git Repository is empty` cho repo được cung cấp. Chưa có source/commit trên GitHub. |
| Website + DB + DB tool (1,5 điểm) | Express/EJS, trang cá nhân, đăng nhập admin, CRUD dự án, sửa hồ sơ, thêm/xóa kỹ năng; MySQL 8.4 và phpMyAdmin | Đủ thành phần ở mức source. Cần build thật, login, CRUD và đối chiếu dữ liệu trong phpMyAdmin; restart kiểm tra dữ liệu còn nguyên. |
| Nginx reverse proxy (1,5 điểm) | `proxy_pass http://app:3000`, forwarded headers, nosniff, DENY, Referrer-Policy; TLS tùy chọn | Cấu hình Compose hợp lệ. Chưa xác nhận Nginx khởi động, headers trả về thực tế và TLS. Đề cho phép security headers cơ bản nên HTTPS không bắt buộc nếu chứng minh headers. |
| Prometheus + Grafana (1,5 điểm) | cAdvisor, Nginx exporter, MySQL exporter; 4 scrape jobs; datasource/dashboard provision sẵn, 10 panels | Chưa có kết quả targets UP, `nginx_up=1`, `mysql_up=1` và metrics container thực. Cần dashboard có dữ liệu; target UP không tự chứng minh toàn bộ panels hoạt động. |
| Loki + Promtail + LogQL (1,5 điểm) | Thu Nginx access/error và app log; Loki datasource; 3 query trong README | Chưa chứng minh ingestion hoặc query trả event thật. Cần ảnh 3 truy vấn và kết quả sau khi tạo request 404/login sai. Phạm vi log là app/Nginx, không phải mọi container. |
| Hardening (1,5 điểm) | USER node, Nginx/Loki/Promtail UID riêng; database internal và không publish MySQL; localhost bindings; cap_drop, no-new-privileges, read-only; mật khẩu ngẫu nhiên; app DB CRUD; CSRF, scrypt, parameterized SQL, rate limit | Có hơn 4 biện pháp ở mức source. Cần UID/process thật, inspect mạng/quyền, SHOW GRANTS và headers. cAdvisor privileged, init containers root và phpMyAdmin là các ngoại lệ cần giải thích. |
| Tổng thể, demo và báo cáo | Hướng dẫn, checklist minh chứng, nhật ký và khung báo cáo | **Chưa hoàn tất.** `KHUNG_BAO_CAO.md` là mẫu có placeholders; không có DOCX/PDF hoàn chỉnh được tìm thấy trong project và `docs/evidence` chỉ có README, chưa có screenshot. Chưa chứng minh đủ 10 trang và bìa thông tin sinh viên. |

Stack thực tế là Node.js/Express/EJS, không phải React/Next.js hoặc PHP. Đề ghi đây là stack *gợi ý*, nên khác framework không tự làm sai yêu cầu; ứng dụng vẫn phải thể hiện đúng portfolio/admin/MySQL.

## Kiểm tra thực hiện trong lượt này

| Kiểm tra | Kết quả |
|---|---|
| Host Node/npm | Node v24.14.0, npm 11.9.0 |
| `npm ci --ignore-scripts` trong app | Thành công từ lockfile |
| `npm test` | 7/7 qua: access control/CSRF/headers, CRUD và escape XSS, URL/input/rate limit, logout, password hashing, ID/URL validation, SQL parameters |
| `npm run check` | Qua |
| `npm audit --omit=dev` | 0 vulnerabilities tại thời điểm chạy; không thay thế kiểm tra ứng dụng/image |
| Compose `config --quiet`, stage 1/2/3 và TLS | Qua, dùng biến môi trường placeholder trong process, không tạo secrets triển khai |
| Python scripts | AST parse qua |
| Grafana dashboard | JSON parse qua |
| Docker | Docker Desktop Engine Linux 29.8.2 truy cập được; Compose v5.6.0 |
| `docker compose ls --format json` | Chỉ thấy một project khác đang chạy; không thấy `de13-portfolio` |
| GitHub | Repo tồn tại nhưng chưa có commit; kiểm tra qua GitHub API |

HTTP tests sử dụng repository thay thế và MemoryStore. Chúng không kiểm chứng MysqlSessionStore, schema init hoặc kết nối DB thật. Không thay nội dung `VALIDATION.md` cũ bằng các khẳng định runtime chưa được kiểm chứng.

## Các điểm cần chú ý khi demo

- Nội dung DB ban đầu còn email `student@example.com`, mô tả và dự án mẫu. Cần cập nhật hồ sơ/dự án thật qua admin trước khi chụp ảnh nộp bài.
- cAdvisor cần host mounts/privileged; trên Docker Desktop phải kiểm tra metrics thực sự xuất hiện trước khi chụp dashboard.
- Có hai file cấu hình datasource Loki (một trong thư mục provisioning, một mount thêm ở stage 3). Kiểm tra cấu hình merge thực tế và provisioning khi chạy; không suy ra lỗi chỉ từ việc tồn tại hai file nguồn.
- Log app và Nginx ghi vào volumes; chưa thấy cấu hình rotation giới hạn dung lượng các file này. Cần theo dõi dung lượng nếu chạy dài ngày.
- Không coi placeholder `.env.example` là secrets dùng để chạy. `setup.py` tạo mật khẩu riêng và từ chối ghi đè.
- Không tuyên bố mọi container non-root: phải giải thích từng ngoại lệ và quyền exporter rộng hơn tài khoản ứng dụng.

## Thứ tự hoàn thiện

1. Chạy `python scripts/setup.py` một lần cho deployment mới; giữ `.env`, `secrets/`, `certs/`, backup ngoài Git.
2. Chạy stage 1; kiểm tra health, admin CRUD, phpMyAdmin và headers. Ghi lại expected/actual và ảnh thật.
3. Khởi tạo Git local, kiểm tra ignore rồi tạo commit 1 cho app/DB/Nginx. Không công khai secrets; không tạo ba commit rỗng để đủ số lượng.
4. Chạy stage 2; kiểm tra targets và dashboard container/web/DB, tạo tải, chụp ảnh; commit 2 cho monitoring.
5. Chạy stage 3; tạo log thử, chạy 3 LogQL queries và chụp ảnh; commit 3 cho logging. Hardening nên được tích hợp và giải thích trong các bước liên quan.
6. Kiểm tra backup/restore, restart, UID, grants và mạng; hoàn thiện README theo kết quả thật. Push các commit lên repository được cung cấp.
7. Viết báo cáo DOCX/PDF tối thiểu 10 trang, bìa đầy đủ họ tên/MSSV/lớp/giảng viên/chủ đề, sơ đồ kiến trúc và ảnh minh chứng thật. Kiểm tra số trang sau khi xuất PDF.

Chưa thay đổi mã ứng dụng, chưa khởi tạo Git, chưa tạo/push commit hoặc triển khai containers trong lượt kiểm tra này.

## Cài đặt skills

- `pbakaus/impeccable`: cài skill `impeccable` từ `.agents/skills/impeccable`.
- `DietrichGebert/ponytail`: cài `ponytail`, `ponytail-audit`, `ponytail-debt`, `ponytail-gain`, `ponytail-help`, `ponytail-review`.
- `mattpocock/skills`: cài các thư mục skill còn thiếu; giữ nguyên bản đã có, không ghi đè các tùy chỉnh hiện hữu. Các skill mới khả dụng từ lượt trao đổi tiếp theo.

Repository: https://github.com/tamtran2k6zz/Website_Portfolio_De13
