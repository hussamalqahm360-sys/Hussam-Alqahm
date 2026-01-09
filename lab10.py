class UserAccount:

    def __init__(self, username, password, email):
        if len(password) < 6:
            raise ValueError("كلمة المرور يجب أن تكون 6 أحرف على الأقل")

        if "@" not in email:
            raise ValueError("البريد الإلكتروني غير صحيح")

        self.username = username
        self.email = email
        self.__password = password
        self.active = True

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old, new):
        if self.__password != old:
            print("كلمة المرور القديمة غير صحيحة ❌")
            return

        if len(new) < 6:
            print("كلمة المرور الجديدة قصيرة ❌")
            return

        self.__password = new
        print("تم تغيير كلمة المرور بنجاح ✅")

    def activate(self):
        self.active = True
        print("تم تفعيل الحساب ✅")

    def deactivate(self):
        self.active = False
        print("تم تعطيل الحساب ⛔")

    def get_info(self):
        return {
            "Username": self.username,
            "Email": self.email,
            "Active": self.active
        }


# مثال تجريبي 

user = UserAccount("Ahmed", "123456", "ahmed@gmail.com")

print(user.get_info())

print(user.check_password("123456"))

user.change_password("123456", "abcdef")

user.deactivate()

print(user.get_info())
