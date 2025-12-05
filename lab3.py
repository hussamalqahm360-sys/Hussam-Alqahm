class Book:
   
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def display_info(self):
     
        print(f"**Book Information:**")
        print(f"   Title: **{self.title}**")
        print(f"   Author: {self.author}")
        print(f"   Year: {self.year}")
        print(f"   Original Price: {self.price:.2f} SAR")

    def discount(self, percent):
    
        if 0 <= percent <= 100:
            final_price = self.price * (1 - (percent / 100))
            return final_price
        return self.price


book1 = Book("AI Fundamentals", "Dr. A. Ali", 2023, 150.00)
book2 = Book("Arabic Literature History", "Dr. F. Zahraa", 2018, 95.50)
book3 = Book("Python Basics", "Eng. K. Ahmed", 2021, 120.75)



print("\n--- Book 1 Details ---")
book1.display_info()
final_price_b1 = book1.discount(15) 
print(f"   Discount (15%): **{final_price_b1:.2f} SAR**")

print("\n--- Book 2 Details ---")
book2.display_info()
final_price_b2 = book2.discount(10) 
print(f"   Discount (10%): **{final_price_b2:.2f} SAR**")

print("\n--- Book 3 Details ---")
book3.display_info()
final_price_b3 = book3.discount(20) 
print(f"   Discount (20%): **{final_price_b3:.2f} SAR**")

