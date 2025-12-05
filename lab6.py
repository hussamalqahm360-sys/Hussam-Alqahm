import pprint

def print_array_status(title, arr):

    print(f"\n--- {title} ---")
    pprint.pprint(arr)
    print("------------------------")

# 1. إنشاء مصفوفة ثنائية الأبعاد
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print_array_status("الحالة الأولية للمصفوفة", matrix)

# 1. إضافة صف
new_row = [100, 110, 120]
matrix.append(new_row)
print_array_status("1. بعد إضافة صف جديد", matrix)

# 2. إضافة عمود
new_column_value = 5
for row in matrix:
    row.append(new_column_value)
print_array_status("2. بعد إضافة عمود جديد (بقيمة 5)", matrix)

# 3. التعديل على عنصر
# تعديل العنصر في الصف رقم 1 والعمود رقم 0 (400 بدلاً من 40)
row_index_to_modify = 1
col_index_to_modify = 0
matrix[row_index_to_modify][col_index_to_modify] = 400
print_array_status("3. بعد التعديل على العنصر [1][0] إلى 400", matrix)

# 4. البحث عن عنصر
search_value = 80
found = False
print(f"\n--- 4. البحث عن العنصر {search_value} ---")
for r_idx, row in enumerate(matrix):
    try:
        c_idx = row.index(search_value)
        print(f"تم العثور على العنصر {search_value} في الموقع: الصف {r_idx}، العمود {c_idx}")
        found = True
        break
    except ValueError:
        continue
if not found:
    print(f"لم يتم العثور على العنصر {search_value} في المصفوفة.")
print("------------------------")

# 5. حذف عمود
# حذف العمود الأخير الذي أضفناه سابقاً (مؤشره هو 3)
column_index_to_delete = 3
for row in matrix:
    if column_index_to_delete < len(row):
        row.pop(column_index_to_delete)
print_array_status("5. بعد حذف العمود رقم 3", matrix)