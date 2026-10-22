---
name: Portfolio Trần Đặng Công Tâm
description: Portfolio học tập với bố cục biên tập và hình minh chứng thật
colors:
  ink: "#102d2b"
  paper: "#f7f8f4"
  muted: "#52645f"
  line: "#d8dfd7"
  accent: "#194d41"
  contact: "#e5ebdd"
typography:
  body:
    fontFamily: "Manrope, system-ui, sans-serif"
    fontSize: "16px"
    lineHeight: 1.7
  display:
    fontFamily: "Manrope, system-ui, sans-serif"
    fontSize: "clamp(42px, 6.5vw, 82px)"
    fontWeight: 500
    lineHeight: 1.04
    letterSpacing: "-0.04em"
  accent:
    fontFamily: "Manrope, system-ui, sans-serif"
    fontWeight: 400
rounded:
  surface: "14px"
  control: "50px"
spacing:
  mobile-gutter: "20px"
  desktop-gutter: "48px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
    padding: "16px 25px"
---

# Portfolio design system

## Overview
Một portfolio biên tập sáng, lấy nội dung và hình ảnh bài thực hành làm trọng tâm. Phong cách được người dùng chấp thuận từ prompt tham khảo studio, chuyển sang ngữ cảnh sinh viên ATTT; không dùng giá dịch vụ, khách hàng hoặc lời chứng thực của người khác.

## Colors
Nền trắng ngà, chữ xanh đen, thông tin phụ xanh xám. Dự án dùng nền pastel theo chủ đề; section liên hệ dùng xanh lá nhạt. Giữ chữ và viền tương phản đủ trên giao diện quản trị.

## Typography
Manrope là font duy nhất cho toàn bộ nội dung, tiêu đề, phần nhấn mạnh và biểu mẫu; không dùng serif hoặc chữ nghiêng. Font tự host trong public/fonts, đi kèm giấy phép OFL. Ảnh chân dung thật và logo ICTU nằm trong cụm thông tin cá nhân đầu trang, giữ tỷ lệ gốc. Tiêu đề chính co giãn theo viewport; body, biểu mẫu và nội dung dự án giữ hệ thống sans để dễ đọc tiếng Việt.

## Layout
Trang chính rộng tối đa 1296px với gutter 48px desktop và 20px mobile. Hero căn giữa; phần dự án mở đầu bằng một ảnh rộng, sau đó hai cột. Dưới 650px chuyển về một cột. Giới thiệu chia hai cột, tiêu đề sticky ở desktop; kỹ năng dạng hàng có đường phân cách. Header và footer giới hạn 1392px. Admin và trang chi tiết dùng app-main 1120px.

## Elevation & Depth
Nền chủ yếu phẳng. Bóng 0 16px 45px #102d2b21 chỉ dùng cho khung screenshot dự án, nghiêng nhẹ và chuyển thẳng khi hover. Không thêm lớp bóng cho mọi section.

## Shapes
Khối ảnh và liên hệ bo 14px; nút chính bo pill. Biểu mẫu dùng viền 1px, nền trắng và radius 7px cho input.

## Components
Nút chính xanh đen, chữ sáng, có focus ring. Link có gạch chân khi hover. Motion dùng IntersectionObserver cho nội dung dưới fold, tiến độ cuộn dùng requestAnimationFrame, không có thư viện animation. Hero, ảnh dự án và liên hệ có cách vào trang khác nhau. Tôn trọng reduced-motion, keyboard focus và nội dung mặc định hiển thị khi không có JavaScript. Dữ liệu hồ sơ/dự án/kỹ năng tiếp tục lấy từ MySQL. Ảnh trong gallery là ảnh minh họa từ Đề 13, nhãn nêu rõ phạm vi; chưa có upload ảnh từng dự án.

## Do's and Don'ts
- Dùng nội dung và minh chứng thật; không suy ra thành tích từ giao diện.
- Giữ CSP, CSRF, session, routes admin và phần escape EJS.
- Không giấu nội dung mặc định trong CSS để chờ JavaScript.
- Giữ ảnh minh họa và font cùng origin để vận hành không phụ thuộc CDN.
- Không thêm hiệu ứng theo con trỏ, GIF liên tục hay auto-carousel không cần thiết.
