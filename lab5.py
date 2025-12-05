student_names = ["أحمد", "فاطمة", "خالد", "سارة", "علي"]
print("1. القائمة الأصلية:", student_names)

my_name = "جميل"
student_names.append(my_name)
print("2. القائمة بعد الإضافة:", student_names)

student_names.remove("خالد")
print("3. القائمة بعد الحذف:", student_names)

num_students = len(student_names)
print(f"4. عدد الطلاب النهائي: {num_students}")

print("\n" + "="*40 + "\n")


student_info = {
    "الاسم": "جميل",
    "الرقم الجامعي": "20230045",
    "التخصص": "علوم الحاسوب",
    "المستوى الدراسي": "الثالث"
}
print("5. القاموس الأصلي:")

for key, value in student_info.items():
    print(f"   {key}: {value}")

student_info["GPA"] = 3.85
print("\n6. القاموس بعد إضافة :")


for key, value in student_info.items():
    print(f"   **{key}:** {value}")

print("\n" + "="*40)

