
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("--- المصفوفة الأصلية ---")
for row in matrix:
    print(row)
print("------------------------\n")


# 1. إضافة صف
def add_row(matrix, new_row_data):
    """يضيف صفاً جديداً."""
    if not matrix or len(new_row_data) == len(matrix[0]):
        matrix.append(new_row_data)
        print(f"✅ 1. تم إضافة الصف: {new_row_data}")
    else:
        print("❌ 1. فشل إضافة الصف.")

# 2. إضافة عمود
def add_column(matrix, new_column_data, col_index=-1):
    """يضيف عموداً جديداً."""
    if len(new_column_data) == len(matrix):
        for i in range(len(matrix)):
            if col_index == -1:
                matrix[i].append(new_column_data[i])
            else:
                matrix[i].insert(col_index, new_column_data[i])
        print(f"✅ 2. تم إضافة عمود بنجاح.")
    else:
        print("❌ 2. فشل إضافة عمود. عدد العناصر لا يساوي عدد الصفوف.")

# 3. التعديل على عنصر
def modify_element(matrix, row_index, col_index, new_value):
    """يعدل قيمة عنصر محدد."""
    try:
        matrix[row_index][col_index] = new_value
        print(f"✅ 3. تم تعديل العنصر في الموقع [{row_index}, {col_index}] إلى {new_value}")
    except IndexError:
        print(f"❌ 3. فشل التعديل. المؤشرات خارج النطاق.")

# 4. البحث عن عنصر
def search_element(matrix, target_value):
    """يبحث عن قيمة محددة."""
    locations = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == target_value:
                locations.append((r, c))
    
    if locations:
        print(f"✅ 4. تم العثور على العنصر '{target_value}' في المواقع: {locations}")
    else:
        print(f"❌ 4. لم يتم العثور على العنصر '{target_value}'.")
    return locations

# 5. حذف عمود
def delete_column(matrix, col_index):
    """يحذف عموداً محدداً."""
    if not matrix or col_index < 0 or col_index >= len(matrix[0]):
        print(f"❌ 5. فشل حذف العمود. المؤشر {col_index} غير صالح.")
        return

    for row in matrix:
        del row[col_index]
    print(f"✅ 5. تم حذف العمود بنجاح في المؤشر: {col_index}")


# ------------------- تنفيذ العمليات -------------------

add_row(matrix, [10, 11, 12]) 
add_column(matrix, [50, 60, 70, 80], col_index=1)
modify_element(matrix, 2, 0, 99)
search_element(matrix, 5)
delete_column(matrix, 1)


print("\n--- المصفوفة النهائية ---")
for row in matrix:
    print(row)
print("------------------------")

