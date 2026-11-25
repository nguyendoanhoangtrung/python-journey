"""Starter for the Week 02 student card."""

name = input("Họ tên: ").strip()
student_id = input("Mã sinh viên: ").strip()
major = input("Ngành: ").strip()
start_year_text = input("Năm nhập học: ").strip()

if not name or not student_id or not major or not start_year_text:
    print("Vui lòng nhập đầy đủ thông tin.")
elif start_year_text.isdigit():
    start_year = int(start_year_text)
    graduation_year = start_year + 4

    print("+------------------------------------------+")
    print(f"| {'THẺ SINH VIÊN':^40} |")
    print("+------------------------------------------+")
    print(f"| {'Họ tên':<18}: {name:<20} |")
    print(f"| {'Mã sinh viên':<18}: {student_id:<20} |")
    print(f"| {'Ngành':<18}: {major:<20} |")
    print(f"| {'Năm nhập học':<18}: {start_year:<20} |")
    print(f"| {'Dự kiến tốt nghiệp':<18}: {graduation_year:<20} |")
    print("+------------------------------------------+")
else:
    print("Năm nhập học cần gồm các chữ số")
