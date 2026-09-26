"""
Cài đặt thuật toán AES (Advanced Encryption Standard)
Sinh viên: Dương Đình Kiền
Môn: An toàn và Bảo mật Thông tin
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import time

def aes_encrypt_decrypt():
    print("=" * 60)
    print("CHUONG TRINH MA HOA/GIAI MA AES-128")
    print("=" * 60)
    
    # 1. Tạo khóa ngẫu nhiên 128-bit (16 bytes)
    key = os.urandom(16)
    print(f"\n[+] Khoa bi mat (128-bit, hex): {key.hex()}")
    
    # 2. Bản rõ cần mã hóa
    message = b"Thong tin bi mat cua sinh vien - Mon Bao Mat Thong Tin"
    print(f"[+] Ban ro: {message.decode('utf-8')}")
    
    # 3. Mã hóa (sử dụng chế độ CBC - Cipher Block Chaining)
    print("\n--- Qua trinh MA HOA ---")
    start_time = time.time()
    
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv  # Vector khởi tạo ngẫu nhiên (16 bytes)
    print(f"[+] IV (Initialization Vector): {iv.hex()}")
    
    # Padding bản rõ cho đủ bội số của 16 bytes
    padded_message = pad(message, AES.block_size)
    print(f"[+] Ban ro sau khi padding: {padded_message.hex()}")
    
    # Mã hóa
    ciphertext = cipher.encrypt(padded_message)
    
    end_time = time.time()
    encrypt_time = end_time - start_time
    print(f"[+] Ban ma (hex): {ciphertext.hex()}")
    print(f"[+] Thoi gian ma hoa: {encrypt_time*1000:.4f} ms")
    
    # 4. Giải mã
    print("\n--- Qua trinh GIAI MA ---")
    start_time = time.time()
    
    decipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_padded = decipher.decrypt(ciphertext)
    
    # Bỏ padding
    decrypted_message = unpad(decrypted_padded, AES.block_size)
    
    end_time = time.time()
    decrypt_time = end_time - start_time
    print(f"[+] Ban ro sau khi giai ma: {decrypted_message.decode('utf-8')}")
    print(f"[+] Thoi gian giai ma: {decrypt_time*1000:.4f} ms")
    
    # 5. Kiểm tra
    print("\n--- Kiem tra ---")
    if message == decrypted_message:
        print("[OK] Ban ro ban dau va ban ro sau giai ma GIONG NHAU!")
    else:
        print("[LOI] Co loi xay ra!")
    
    print("=" * 60)

if __name__ == "__main__":
    aes_encrypt_decrypt()