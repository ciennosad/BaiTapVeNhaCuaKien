\# Bài Tập Về Nhà - 2 Môn



\## Thông tin sinh viên

\- \*\*Họ tên:\*\* Dương Đình Kiền

\- \*\*MSSV:\*\* K235480106109

\- \*\*Email:\*\* kienduon757@gmail.com



\## Môn 1: An toàn và bảo mật thông tin

1\. tìm hiểu thuật toán mã hoá hiện đại DES, AES

&#x20;  mô tả đc thuật toán, quy trình mã hoá/giải mã

&#x20;  cài đặt AES trên 1 ngôn ngữ lập trình nào đó

2\. tìm hiểu về thuật toán mã hoá bất đối xứng RSA

&#x20;  nguyên lý sinh cặp khoá bí mật, công khai

3\. trình bày các mô hình hình áp dụng thuật toán RSA

&#x20;  xác thực người gửi, xác thực người nhận, cả 2

&#x20;  so sánh thời gian mã hoá/giải mã của RSA với AES.

&#x20;  đưa ra các dùng kết hợp sức mạnh của RSA và AES.



\## CẤU TRÚC THƯ MỤC:



MÔN BẢO MẬT THÔNG TIN/

\-BAO-CAO-DÉ-AES-RSA.md# Báo cáo lý thuyết

\-Code-AES/: + aes\_demo.py@ code cài đặt AES

\-images/

\-aes\_result.png #Ảnh kết quả chạy AES



\## Môn 2: Lập trình web

\- Docker Compose

\- Nginx

\- Node-RED

\- API



bài tập 1:

1\. giả lập linux os: hyperV, virtualBox, vmware, wsl

2\. cài đặt docker compose trên os đó

3\. cài trên docker compose : các dịch vụ: nginx, nodered, mariadb, phpmyadmin, cloudflared (cần domain xịn)

4\. cấu hình nginx có thể chạy 2 website  với 2 domain khác nhau.

- Giả lập Linux OS bằng WSL2 (Ubuntu).
- Cài đặt Docker và triển khai 5 dịch vụ: `nginx`, `nodered`, `mariadb`, `phpmyadmin`, `cloudflared`.
- **Domain:** Sử dụng domain thật `web-tiet-kiem.id.vn` (đăng ký miễn phí tại Mắt Bão).
- **Cloudflare Tunnel:** Đã tạo Tunnel với Token thật, cấu hình Public Hostname trỏ về dịch vụ trong Docker.
- **Cấu hình Nginx:** Chạy 2 website:
  - Site 1: `web.web-tiet-kiem.id.vn` (có tích hợp gọi API)
  - Site 2: `site2.local` (website đơn giản chạy local)



bài tập 2:

1\. sử dụng nodered: dùng node http\_in + http\_response => tạo api đơn giản

2\. cấu hình nginx để web dùng js gọi đc API trên nodered, thuật toán cho api (tự nghĩ)

&#x20;  ví dụ api trả về json:

&#x20;  https://tnut.cuong.id.vn/api/tacke

&#x20;  trả về json dạng:

&#x20;  {"ok":1,"msg":"thành công","dssv":\[{"name":"Cốp","money":123},{"name":"David","money":456}]}

3\. code js vào trang html để gọi đc api trên

- Tạo API đơn giản trên Node-RED trả về JSON danh sách sinh viên (`/api/tacke`).
- Cấu hình Nginx Reverse Proxy để website có thể gọi API từ Node-RED.
- Viết mã JavaScript (Fetch API) trong file HTML để gọi và hiển thị dữ liệu.
##Bài làm 
### Link demo thực tế:
- Website Site 1: [https://web.web-tiet-kiem.id.vn](https://web.web-tiet-kiem.id.vn)
- Website Site 2: [http://site2.local/]
- Mở ubuntu chạy lệnh:  cd ~/Mon_Lap_Trinh_Web
                        sudo docker compose ps
- website http://localhost:1880/api/tacke
{"ok":1,"msg":"thành công","dssv":[{"name":"Cốp","money":123},{"name":"David","money":456},{"name":"kienday","money":999},{"name":"Lan","money":750},{"name":"Dương Đình Kiền","money":673},{"name":"Kiền Nè","money":990}]}

\## CẤU TRÚC THƯ MỤC:

Mon\_Lap\_Trinh-Web/

\-docker-compose.yml # File cấu hình Docker

\-nginx/

+conf.d/

+site1.conf# Cònig Nginx cho site 1

+site2.conf# Confif Nginx cho site 2

\-Web/

+site 1/

++index.html #web gọi API

+site2/

++index.html #web đơn giản

\-images/

\-noderes\_flow.png

\-api\_test.png #Test API 

\-Web\_call\_api.png #web gọi API





\### Ảnh minh chứng:

\- \[Flow Node-RED](./Mon\_Lap\_Trinh\_Web/images/nodered\_flow.png)

\- \[Test API trực tiếp](./Mon\_Lap\_Trinh\_Web/images/api\_test.png)

\- \[Website gọi API thành công](./Mon\_Lap\_Trinh\_Web/images/web\_call\_api.png)





\## Deadline

23h59 ngày 28/9/2026

