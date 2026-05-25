hospital_name = "BỆNH VIỆN ĐA KHOA SỨC KHỎE VÀNG"
kiosk_title = "KIOSK ĐĂNG KÝ TỰ PHỤC VỤ (HỆ THỐNG THÔNG MINH)"
separator = "=" * 60
short_separator = "-" * 30

print(separator)
print(hospital_name.center(60))
print(kiosk_title.center(60))
print(separator)
print("\nChào mừng quý bệnh nhân! Vui lòng nhập thông tin theo hướng dẫn.\n")


raw_full_name = input("1. Nhập Họ và Tên (Ví dụ: Nguyễn Văn A): ")
raw_id = input("2. Nhập Mã bệnh nhân (Ví dụ: BN999): ")
raw_temp = input("3. Nhập Nhiệt độ cơ thể (Ví dụ: 36.5 hoặc 37): ")
raw_heart_rate = input("4. Nhập Nhịp tim - bpm (Ví dụ: 80): ")
raw_weight = input("5. Nhập Cân nặng - kg (Ví dụ: 65.5): ")


patient_full_name = str(raw_full_name).upper() 
patient_id = str(raw_id)
body_temperature = float(raw_temp) 
heart_rate = int(raw_heart_rate) 
body_weight = float(raw_weight) 

print("\n" + separator)
print("PHIẾU KHÁM BỆNH ĐIỆN TỬ".center(60))
print(separator)
print(f"Họ tên bệnh nhân: {patient_full_name}")
print(f"Mã số định danh: {patient_id}")
print(short_separator)
print("CHỈ SỐ SINH HIỆU (Ghi nhận lúc tiếp nhận):")
print(f"- Nhiệt độ cơ thể: {body_temperature}°C")
print(f"- Nhịp tim: {heart_rate} nhịp/phút (bpm)")
print(f"- Cân nặng: {body_weight} kg")
print(short_separator)
print("Trạng thái: Đã sẵn sàng. Mời bệnh nhân chờ tại khu vực Phòng Khám.")
print(separator)

print("\n[HỆ THỐNG IT] - LOG CHUẨN HÓA DỮ LIỆU (SYSTEM LOGS):")
print(f"Variable: patient_full_name | Value: {patient_full_name} | Type: {type(patient_full_name)}")
print(f"Variable: patient_id | Value: {patient_id} | Type: {type(patient_id)}")
print(f"Variable: body_temperature | Value: {body_temperature} | Type: {type(body_temperature)}")
print(f"Variable: heart_rate | Value: {heart_rate} | Type: {type(heart_rate)}")
print(f"Variable: body_weight | Value: {body_weight} | Type: {type(body_weight)}")
print("[!] Dữ liệu đã được chuẩn hóa. Kết nối Monitor: Ổn định.\n")
