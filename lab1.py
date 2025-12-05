class students:
    def __init__(self, name, grad):
        self.name = name
        self.grad = grad

    def is_passed(self):
        if self.grad >= 50:
            return "ناجح"
        else:
            return "راسب"


student_list = [
    students("محمد", 88),
    students("سارة", 45),
    students("خالد", 92),
    students("ليلى", 30),
    students("علي", 65),
    students("نور", 50)
]


passed_students_names = []
failed_students_names = []


print("نتائج الطلاب الفردية:")
print("-" * 30)

for student in student_list:
    result = student.is_passed()
    print(f"الطالب {student.name}: التقدير: {result}")
    
    if result == "ناجح":
        passed_students_names.append(student.name)
    else:
        failed_students_names.append(student.name)


print("\n" + "=" * 40)
print("## ملخص نتائج الصف ##")
print("=" * 40)

print(f"✅ عدد الطلاب الناجحين: **{len(passed_students_names)}**")
print(f"   أسماء الناجحين: {passed_students_names}")

print(f"\n❌ عدد الطلاب الراسبين: **{len(failed_students_names)}**")
print(f"   أسماء الراسبين: {failed_students_names}")
print("=" * 40)

