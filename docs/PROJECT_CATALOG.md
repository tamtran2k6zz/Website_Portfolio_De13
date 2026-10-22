# Danh mục dự án cá nhân

Bốn dự án được giới thiệu theo README của các repository liên kết trong
`db/portfolio-projects.json`. SmartBus và Smart Clinic là dự án nhóm.
Ba ảnh giao diện do chủ portfolio cung cấp được lưu tại `app/public/images/`:
EduQuiz (`eduquiz.webp`), SmartBus (`smartbus.webp`), Smart Clinic (`clinic.webp`).
ZShop chưa có ảnh; giao diện hiển thị trạng thái này thay vì ảnh dự án khác.
Ảnh trang chủ Portfolio do chủ portfolio cung cấp được lưu tại
`app/public/images/portfolio-home.webp`; Portfolio đứng đầu danh sách.

Sau khi stack hoạt động, sao lưu và đồng bộ nội dung:

```powershell
python scripts/backup.py
python scripts/sync-portfolio-projects.py
```

Script cập nhật dự án Portfolio ID 7 và thêm/cập nhật bốn dự án theo URL GitHub,
trong một transaction. Chạy lại không tạo bản ghi trùng. Không xóa dự án khác
hoặc thay đổi hồ sơ cá nhân. Nội dung mô tả vẫn có thể chỉnh trong trang admin;
chạy lại script sẽ áp dụng lại nội dung trong JSON cho bốn dự án này.

Để giữ đúng năm dự án chính và xóa các dự án mẫu khác (sao lưu trước):

```powershell
python scripts/backup.py
python scripts/sync-portfolio-projects.py --only-catalog
```

Ảnh được ghép theo URL repository trong `app/src/project-visual.js`.
Các chức năng giới thiệu dựa trên README, không phải xác nhận đã triển khai
hoặc kiểm thử các repository bên ngoài. Thanh toán ZShop là mô phỏng.
