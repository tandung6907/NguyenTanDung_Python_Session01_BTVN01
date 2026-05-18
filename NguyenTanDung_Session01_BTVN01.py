# Phân tích lỗi:
#   - Chương trình không crash vì cú pháp hoàn toàn hợp lệ
#   - Bug nằm ở logic: hai biến name_patient và age bị hoán đổi khi in ra
#   - print('Tên bệnh nhân:', symptom) -> in triệu chứng vào chỗ tên
#   - print('Tuổi:', name_patient)    -> in tên vào chỗ tuổi
#   - print('Triệu chứng:', age)      -> in tuổi vào chỗ triệu chứng
#   => Kết quả ra phiếu hoàn toàn sai dù chương trình chạy bình thường

def legacy_code():
    print('\n--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN (LEGACY - CÓ LỖI) ---');
    name_patient = input('Nhập tên bệnh nhân: ');
    age          = input('Nhập tuổi bệnh nhân: ');
    symptom      = input('Mô bạn nhập khẩu chứng bệnh: ');

    print('\n--- PHIẾU KHÁM BỆNH ---');
    print('Tên bệnh nhân:', symptom);      # LỖI: in symptom thay vì name_patient
    print('Tuổi:', name_patient);          # LỖI: in name_patient thay vì age
    print('Triệu chứng:', age);            # LỖI: in age thay vì symptom

legacy_code();


# Sửa lỗi:
# Nguyên nhân lỗi gốc: lập trình viên truyền sai biến vào hàm print,
# có thể do copy-paste hoặc nhầm thứ tự biến.
# Cách sửa: đưa đúng biến vào đúng vị trí in.

def fixed_code():
    print('\n--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---');
    name_patient = input('Nhập tên bệnh nhân: ');
    age          = input('Nhập tuổi bệnh nhân: ');
    symptom      = input('Mô tả triệu chứng bệnh: ');

    print('\n--- PHIẾU KHÁM BỆNH ---');
    print('Tên bệnh nhân:', name_patient);  # Đã sửa: dùng đúng biến name_patient
    print('Tuổi:', age);                    # Đã sửa: dùng đúng biến age
    print('Triệu chứng:', symptom);         # Đã sửa: dùng đúng biến symptom

fixed_code();
