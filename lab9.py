class Node:
    """يمثل عقدة فردية في القائمة المرتبطة."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """يمثل هيكل بيانات القائمة المرتبطة ويدير العمليات عليها."""
    def __init__(self):
        self.head = None  # مؤشر الرأس

    # 1. إضافة عقدة في بداية القائمة (الرأس) - O(1)
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"✅ تمت إضافة {data} في الرأس.")

    # 2. إضافة عقدة في نهاية القائمة (الذيل) - O(n)
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"✅ تمت إضافة {data} في الذيل.")
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print(f"✅ تمت إضافة {data} في الذيل.")

    # 3. البحث عن قيمة معينة - O(n)
    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                print(f"🔎 تم العثور على القيمة {key} في الموضع {position}.")
                return True
            current = current.next
            position += 1
        print(f"❌ القيمة {key} غير موجودة.")
        return False

    # 4. حذف عقدة تحمل قيمة معينة - O(n)
    def delete(self, key):
        current = self.head
        prev = None

        # حالة الحذف من الرأس
        if current and current.data == key:
            self.head = current.next
            print(f"🗑️ تم حذف {key} من الرأس.")
            return

        # البحث عن العقدة المراد حذفها
        while current and current.data != key:
            prev = current
            current = current.next

        # القيمة غير موجودة
        if current is None:
            print(f"❌ لا يمكن الحذف: القيمة {key} غير موجودة.")
            return

        # الحذف من المنتصف أو الذيل
        prev.next = current.next
        print(f"🗑️ تم حذف {key} بنجاح.")

    # 5. طباعة جميع عناصر القائمة
    def print_list(self):
        current = self.head
        if not current:
            print("القائمة فارغة.")
            return

        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("القائمة: " + " -> ".join(elements))

    # 6. الدالة الجديدة: حساب عدد العقد - O(n)
    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# --- مثال على الاستخدام ---
my_list = LinkedList()
my_list.insert_at_head(5)
my_list.insert_at_tail(20)
my_list.insert_at_head(1)
my_list.insert_at_tail(30)
my_list.print_list()  # القائمة: 1 -> 5 -> 20 -> 30

my_list.search(20)
my_list.delete(5)

print("\n")
my_list.print_list()  # القائمة: 1 -> 20 -> 30

node_count = my_list.count_nodes()
print(f"⭐ عدد العقد النهائي في القائمة: {node_count}")

