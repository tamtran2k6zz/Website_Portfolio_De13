# Giao diện portfolio và animation theo cuộn

Ngày cập nhật: 22/10/2026.

Đợt chỉnh sửa bổ sung cùng ngày: thống nhất một font Manrope cho tiêu đề, nội dung, nút và biểu mẫu; bỏ serif/chữ nghiêng. Thêm ảnh chân dung và logo ICTU do chủ portfolio cung cấp vào cụm nhận diện đầu trang. Ảnh được tối ưu WebP, giữ đủ khung hình và không lưu EXIF; file gốc giữ nguyên ngoài project. Browser kiểm tra font computed, ảnh tải đủ và màn hình 320/390/1440px đều qua. Font Newsreader không còn sử dụng.

Trang công khai được thiết kế lại theo hướng biên tập sáng, dùng Manrope tự host (giấy phép OFL kèm font). Bố cục gồm giới thiệu, dự án, giới thiệu cá nhân, kỹ năng và liên hệ. Dữ liệu vẫn từ MySQL; Express/EJS và các route admin/CSRF không thay kiến trúc.

Animation sử dụng CSS và IntersectionObserver: hero vào trang, dự án và nội dung xuất hiện khi cuộn, ảnh thẳng nhẹ khi hover, tiến độ đọc ở đầu trang. Mặc định nội dung hiển thị; thiếu JavaScript/IntersectionObserver không làm mất nội dung. Reduced-motion tắt chuyển động; focus bàn phím làm hiện nội dung tương ứng. Không có carousel tự chạy, thư viện animation hoặc tracking bên ngoài.

Ảnh dự án là bộ minh chứng Đề 13 được phân loại theo tên/công nghệ và ghi nhãn minh họa, chưa phải ảnh riêng do admin upload. Profile, kỹ năng, title/description/stack/link vẫn chỉnh được từ admin. Font và ảnh cùng origin, không mở rộng CSP cho CDN.

## Kiểm chứng

- 7/7 tests hiện có qua; Node syntax checks qua.
- Docker app build và khởi động healthy; đăng nhập admin qua giao diện thành công.
- Browser kiểm tra desktop 1440, tablet 768, mobile 390 và 320px: không tràn ngang.
- Scroll reveal hoạt động; cuộn toàn trang không còn nội dung pending; tất cả ảnh tải được.
- Reduced-motion không có animation; khi tắt JS, nội dung vẫn hiển thị.
- Browser không có page error hoặc console error trong ca kiểm tra.
- Ảnh xem trước và snapshot kiểm tra: `docs/evidence/redesign/`.

Báo cáo Word và ảnh nghiệm thu ngày 18/10/2026 lưu lại giao diện cũ tại thời điểm nghiệm thu; đợt này chỉ cập nhật website và tài liệu giao diện, không viết lại báo cáo.
