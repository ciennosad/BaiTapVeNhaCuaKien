\# Báo cáo Môn An toàn và Bảo mật Thông tin



\## Sinh viên

\- \*\*Họ tên:\*\* Dương Đình Kiền

\- \*\*MSSV:\*\* K235480106109

\- \*\*Email:\*\* kienduon757@gmail.com



\---



\## 1. Thuật toán DES (Data Encryption Standard)



\### 1.1. Mô tả

\- DES là thuật toán mã hóa khối (block cipher) đối xứng, được công bố năm 1977.

\- Sử dụng khóa \*\*56-bit\*\* (thực tế 64-bit, trong đó 8 bit dùng để kiểm tra chẵn lẻ).

\- Mã hóa từng khối dữ liệu \*\*64-bit\*\*.



\### 1.2. Quy trình mã hóa

1\. \*\*Hoán vị đầu (Initial Permutation - IP):\*\* Sắp xếp lại 64 bit đầu vào.

2\. \*\*16 vòng Feistel:\*\* Mỗi vòng thực hiện:

&#x20;  - Chia khối 64-bit thành 2 nửa L và R (mỗi nửa 32-bit).

&#x20;  - Hàm F: R được mở rộng từ 32-bit lên 48-bit, XOR với khóa vòng, đi qua 8 hộp S (S-box), hoán vị P.

&#x20;  - L\_new = R\_old, R\_new = L\_old XOR F(R\_old, K\_i).

3\. \*\*Hoán vị cuối (Final Permutation - FP):\*\* Sắp xếp lại để tạo bản mã 64-bit.



\### 1.3. Quy trình giải mã

\- Giống hệt mã hóa nhưng \*\*thứ tự khóa vòng bị đảo ngược\*\* (K\_16 → K\_1).



\### 1.4. Nhược điểm

\- Khóa 56-bit quá ngắn → dễ bị tấn công vét cạn (brute-force).

\- Đã bị phá vỡ thực tế năm 1999 (EFF DES cracker trong 22 giờ).

\- \*\*Hiện trạng:\*\* Không còn được khuyến nghị sử dụng.



\---



\## 2. Thuật toán AES (Advanced Encryption Standard)



\### 2.1. Mô tả

\- AES là thuật toán mã hóa khối đối xứng, được NIST chọn làm chuẩn năm 2001.

\- Mã hóa từng khối \*\*128-bit\*\*.

\- Hỗ trợ 3 độ dài khóa: \*\*128-bit, 192-bit, 256-bit\*\*.

\- Số vòng lặp: 10 vòng (128-bit), 12 vòng (192-bit), 14 vòng (256-bit).



\### 2.2. Quy trình mã hóa (1 vòng)

Mỗi vòng (trừ vòng cuối) thực hiện 4 bước:

1\. \*\*SubBytes:\*\* Thay thế mỗi byte bằng byte tương ứng trong bảng S-box (dựa trên phép nghịch đảo trong trường GF(2^8)).

2\. \*\*ShiftRows:\*\* Dịch chuyển cyclic các hàng của ma trận trạng thái 4x4.

3\. \*\*MixColumns:\*\* Nhân mỗi cột của ma trận trạng thái với ma trận cố định trong GF(2^8).

4\. \*\*AddRoundKey:\*\* XOR ma trận trạng thái với khóa vòng.



\*\*Vòng cuối cùng\*\* bỏ qua bước MixColumns.



\### 2.3. Quy trình giải mã

\- Thực hiện ngược lại: InvShiftRows → InvSubBytes → AddRoundKey → InvMixColumns.

\- Thứ tự khóa vòng cũng bị đảo ngược.



\### 2.4. Ưu điểm

\- Tốc độ nhanh, hiệu quả cả phần cứng và phần mềm.

\- An toàn cao, chưa bị phá vỡ thực tế.

\- Được sử dụng rộng rãi (HTTPS, VPN, WiFi WPA2, file encryption...).



\---



\## 3. Thuật toán RSA (Rivest-Shamir-Adleman)



\### 3.1. Nguyên lý sinh cặp khóa

RSA là thuật toán mã hóa \*\*bất đối xứng\*\* (asymmetric), sử dụng 2 khóa khác nhau.



\*\*Quy trình sinh khóa:\*\*

1\. Chọn 2 số nguyên tố lớn \*\*p\*\* và \*\*q\*\* (thường > 1024-bit).

2\. Tính \*\*n = p × q\*\* (modulus, thường 2048-bit hoặc 4096-bit).

3\. Tính \*\*φ(n) = (p-1)(q-1)\*\* (hàm Euler).

4\. Chọn số \*\*e\*\* sao cho: 1 < e < φ(n) và gcd(e, φ(n)) = 1. Thường chọn \*\*e = 65537\*\*.

5\. Tính \*\*d\*\* sao cho: \*\*(d × e) mod φ(n) = 1\*\* (d là nghịch đảo modular của e).



\*\*Cặp khóa:\*\*

\- \*\*Khóa công khai (Public Key):\*\* (e, n) → dùng để \*\*mã hóa\*\*.

\- \*\*Khóa bí mật (Private Key):\*\* (d, n) → dùng để \*\*giải mã\*\*.



\### 3.2. Mã hóa và giải mã

\- \*\*Mã hóa:\*\* C = M^e mod n (M là bản rõ, C là bản mã)

\- \*\*Giải mã:\*\* M = C^d mod n



\---



\## 4. Các mô hình áp dụng RSA



\### 4.1. Mô hình 1: Xác thực người gửi (Chữ ký số)

\- \*\*Người gửi:\*\* Dùng \*\*Private Key\*\* của mình để ký (mã hóa) thông điệp → tạo chữ ký số.

\- \*\*Người nhận:\*\* Dùng \*\*Public Key\*\* của người gửi để xác minh chữ ký.

\- \*\*Mục đích:\*\* Đảm bảo thông điệp thực sự đến từ người gửi (không thể giả mạo).



\### 4.2. Mô hình 2: Xác thực người nhận (Mã hóa bí mật)

\- \*\*Người gửi:\*\* Dùng \*\*Public Key\*\* của người nhận để mã hóa thông điệp.

\- \*\*Người nhận:\*\* Dùng \*\*Private Key\*\* của mình để giải mã.

\- \*\*Mục đích:\*\* Chỉ người nhận mới đọc được nội dung (bí mật).



\### 4.3. Mô hình 3: Kết hợp cả 2 (Xác thực + Bí mật)

\- \*\*Người gửi:\*\* 

&#x20; 1. Ký thông điệp bằng \*\*Private Key\*\* của mình → tạo chữ ký.

&#x20; 2. Mã hóa (thông điệp + chữ ký) bằng \*\*Public Key\*\* của người nhận.

\- \*\*Người nhận:\*\*

&#x20; 1. Giải mã bằng \*\*Private Key\*\* của mình.

&#x20; 2. Xác minh chữ ký bằng \*\*Public Key\*\* của người gửi.

\- \*\*Mục đích:\*\* Vừa đảm bảo bí mật, vừa xác thực nguồn gốc.



\---



\## 5. So sánh thời gian mã hóa/giải mã RSA và AES



| Tiêu chí | AES (đối xứng) | RSA (bất đối xứng) |

|----------|----------------|---------------------|

| \*\*Độ dài khóa\*\* | 128/192/256-bit | 2048/4096-bit |

| \*\*Tốc độ mã hóa\*\* | \*\*Rất nhanh\*\* | Chậm hơn AES \~100-1000 lần |

| \*\*Tốc độ giải mã\*\* | \*\*Rất nhanh\*\* | Chậm hơn AES \~100-1000 lần |

| \*\*Phù hợp với\*\* | Dữ liệu lớn (file, stream) | Dữ liệu nhỏ (khóa, chữ ký) |

| \*\*Độ an toàn\*\* | Cao (chưa bị phá) | Cao (phụ thuộc độ dài khóa) |



\*\*Kết luận:\*\* AES nhanh hơn RSA rất nhiều lần do RSA phải tính toán với số nguyên lớn (modular exponentiation).



\---



\## 6. Kết hợp sức mạnh của RSA và AES (Hybrid Encryption)



\### 6.1. Nguyên lý

\- Dùng \*\*RSA\*\* để mã hóa/truyền \*\*khóa của AES\*\* (vì khóa AES chỉ 128-256 bit, RSA xử lý tốt).

\- Dùng \*\*AES\*\* để mã hóa \*\*toàn bộ dữ liệu thực tế\*\* (vì AES nhanh, phù hợp dữ liệu lớn).



\### 6.2. Quy trình

1\. Người gửi tạo ngẫu nhiên \*\*khóa AES\*\* (session key).

2\. Người gửi mã hóa \*\*dữ liệu\*\* bằng \*\*khóa AES\*\* → nhanh.

3\. Người gửi mã hóa \*\*khóa AES\*\* bằng \*\*Public Key RSA\*\* của người nhận → an toàn.

4\. Gửi cả \*\*dữ liệu đã mã hóa AES\*\* + \*\*khóa AES đã mã hóa RSA\*\* cho người nhận.

5\. Người nhận giải mã \*\*khóa AES\*\* bằng \*\*Private Key RSA\*\* của mình.

6\. Người nhận giải mã \*\*dữ liệu\*\* bằng \*\*khóa AES\*\* vừa nhận được.



\### 6.3. Ứng dụng thực tế

\- \*\*HTTPS/SSL/TLS:\*\* Dùng RSA để trao đổi khóa, AES để mã hóa dữ liệu web.

\- \*\*PGP/GPG:\*\* Mã hóa email.

\- \*\*VPN:\*\* Thiết lập kênh bảo mật.



\---



\## 7. Cài đặt thuật toán AES



Xem file `Code\_AES/aes\_demo.py` trong thư mục này.



\### Kết quả chạy chương trình

<img src="./images/aes\_result.png" alt="Kết quả chạy AES">

