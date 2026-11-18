"""
Bài tập 02: Máy tính Python 🧮
================================
Mục tiêu: Sử dụng các phép tính cơ bản trong Python
"""

# TODO 1: Tính và in ra kết quả của 2024 + 1000
print("TODO 1:")
print("2024 + 1000 =", 2024 + 1000)

# TODO 2: Bạn có 150,000 VNĐ, mua 3 ly cà phê giá 35,000 VNĐ/ly.
# Tính và in ra số tiền còn lại.
print("TODO 2:")
tien_ban_dau = 150000
gia_ca_phe = 35000
so_ly = 3

print(f"Số tiền còn lại: {tien_ban_dau} - {gia_ca_phe} * {so_ly} =", tien_ban_dau - gia_ca_phe * so_ly, "VNĐ")

# TODO 3: Tính diện tích hình tròn có bán kính = 7
# Gợi ý: Diện tích = 3.14159 * bán_kính ** 2
print("TODO 3:")
ban_kinh = 7
dien_tich = 3.14159 * ban_kinh ** 2

print(f"Diện tích hình tròn: 3.14159 * {ban_kinh} ** 2 = ", dien_tich)

# TODO 4: Bạn có 100 viên kẹo chia đều cho 7 người.
# In ra: mỗi người được bao nhiêu viên (chia nguyên)?
# In ra: còn dư bao nhiêu viên?
# Gợi ý: Dùng // và %
print("TODO 4:")
so_keo = 100
so_nguoi = 7

moi_nguoi = so_keo // so_nguoi
keo_con_du = so_keo % so_nguoi

print("Mỗi người được:", moi_nguoi, "viên kẹo")
print("Số kẹo còn dư:", keo_con_du, "viên")
# TODO 5 (Thử thách): Chuyển đổi 37 độ C sang Fahrenheit
# Công thức: F = C * 9/5 + 32
# In ra kết quả dạng: "37°C = ???°F"
print("TODO 5:")
do_C = 37
do_F = do_C * 9 / 5 + 32

print(f"{do_C}°C = {do_F}°F")
