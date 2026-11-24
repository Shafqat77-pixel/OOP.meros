#Uyishi1
# class User:
#     def __init__(self, name, email, address):
#         self.name = name 
#         self.email = email 
#         self.address = address

#     def get_email(self):
#         return self.email

#     def get_name(self):
#         return self.name

#     def get_address(self):
#         return self.address

#     def set_address(self, new_address):
#         self.address = new_address

#     def __str__(self):
#         return f"""User: {self.name} <{self.email}>"""

# class Customer(User):
#     def __init__(self, name, email, address, balance):
#         super().__init__(name, email, address)
#         self.cart = [] 
#         self.balance = balance

#     def add_to_cart(self, product, qty, price):
#         if qty>0 and price>0:
#             self.cart.append((product, qty, price))

#     def clear_cart(self):
#         self.cart.clear()

#     def get_cart_total(self):
#         yegindi = 0
#         for mahsulot in self.cart:
#             yegindi += mahsulot[-1] * mahsulot[1]
#         return yegindi

#     def checkout(self):
#         if self.get_cart_total() <= self.balance:
#             self.balance -= self.get_cart_total()
#             self.clear_cart()
#             return True
#         return False

#     def __str__(self):
#         return f"Customer: {self.name} ({self.balance} so'm)"
# class Seller(User):
#     def __init__(self, ism, email, manzil, rating=0):
#         super().__init__(ism, email, manzil)
#         self.products = {}
#         self.rating = rating

#     def add_product(self, name, qty):
#         if name not in self.products:
#             self.products[name] = qty 
#         else:
#             self.products[name] += qty

#     def remove_product(self, name):
#         if name in self.products:
#             self.products.pop(name)
#             return True
#         else:
#             return False

#     def update_stock(self, name, delte_qty):
#         if name in self.products and self.products[name] + delte_qty >= 0:
#             self.products[name] += delte_qty
#             return True
#         return False 
    
#     def get_stock(self):
#         return self.products.copy()

#     def __str__(self):
#         return F"Seller: {self.name} (rating: {self.rating}, items: {sum(self.products.values())})"
    

# c = Customer("Ali", "ali@mail.com", "Toshkent", balance=2_000_000)
# c.add_to_cart("Keyboard", 1, 300_000)
# c.add_to_cart("Mouse", 2, 150_000)
# print(c.get_cart_total())           
# s = Seller("Gulbahor", "g@mail.com", "Samarqand", rating=4.8)
# s.add_product("Keyboard", 10)
# s.update_stock("Keyboard", -3)
# print(s.get_stock())   











        








#uyishi3
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher 
#         self.students = []

#     def get_title(self):
#         return self.title

#     def get_teacher(self):
#         return self.teacher

#     def enroll(self, student_name: str):
#         if student_name not in self.students:
#             self.students.append(student_name)
#             return True 
#         return False

#     def drop(self, student_name: str):
#         if student_name in self.students:
#             self.students.remove(student_name)
#             return True
#         return False

#     def __str__(self):
#         return f"Course: {self.title} ({self.teacher})"

# class OnlineCourse(Course):
#     def __init__(self, title, teacher, url, max_students):
#         super().__init__(title, teacher)
#         self.url = url 
#         self.max_std = max_students

#     def enroll(self, student_name):
#         return len(self.students) < self.max_std and super().enroll(student_name)

#     def get_room(self):
#         return f"Virtual: {self.url}"

# class OfflineCourse(Course):
#     def __init__(self, title, teacher, room, capacity):
#         super().__init__(title, teacher)
#         self.room = room
#         self.capacity = capacity

#     def enroll(self, student_name):
#         return len(self.students)<self.capacity and super().enroll(student_name)

#     def get_room(self):
#         return f"Room: {self.room}"


# o = OnlineCourse("Python Basics", "Guzal", url="https://nt.uz/py", max_students=2)
# print(o.enroll("Ali")) 

# f = OfflineCourse("Algorithms", "Dilshod", room="B-203", capacity=1)
# print(f.enroll("Soliha"))