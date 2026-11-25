"""
Bài tập 03: Máy tính nhận input 🖥️
====================================
Mục tiêu: Kết hợp input() với tính toán
"""

# TODO 1: Nhập 2 số từ người dùng, in ra tổng, hiệu, tích, thương
so_thu_nhat = float(input("Nhập số thứ nhất: "))
so_thu_hai = float(input("Nhập số thứ hai: "))
print("Tổng:", so_thu_nhat + so_thu_hai)
print("Hiệu:", so_thu_nhat - so_thu_hai)
print("Tích:", so_thu_nhat * so_thu_hai)
if so_thu_hai != 0:
    print("Thương:", so_thu_nhat / so_thu_hai)
else:
    print("Không thể tính thương vì số thứ hai bằng 0.")


# TODO 2: Nhập bán kính hình tròn, tính và in:
# - Diện tích = π × r²
# - Chu vi = 2 × π × r
# Dùng pi = 3.14159
pi = 3.14159
ban_kinh = float(input("Nhập bán kính hình tròn: "))
dien_tich = pi * ban_kinh**2
chu_vi = 2 * pi * ban_kinh
print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)


# TODO 3: Nhập giá gốc và % giảm giá
# Tính và in giá sau khi giảm
# Ví dụ: Giá gốc 500,000, giảm 20% → 400,000
gia_goc = float(input("Nhập giá gốc: "))
phan_tram_giam = float(input("Nhập phần trăm giảm giá: "))
gia_sau_khi_giam = gia_goc * (1 - phan_tram_giam / 100)
print("Giá sau khi giảm:", gia_sau_khi_giam)


# TODO 4 (Thử thách): Máy đổi tiền
# Nhập số tiền VNĐ, tỷ giá USD/VNĐ
# In ra số USD tương ứng (làm tròn 2 chữ số)
so_tien_vnd = float(input("Nhập số tiền VNĐ: "))
ty_gia = float(input("Nhập tỷ giá USD/VNĐ: "))
so_tien_usd = so_tien_vnd / ty_gia
print(f"Số tiền USD: {so_tien_usd:.2f}")
