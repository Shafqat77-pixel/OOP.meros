#m1
# class BookStore:
#     def __init__(self,name,age,book_name,book_price):
#         self.name=name
#         self.age=age
#         self.book_name=book_name
#         self.book_price=book_price
#     def info(self):
#         print(f"""Name: {self.name}
# Age: {self.age}
# Book_name: {self.book_name}
# Book price: {self.book_price*(100-self.age)/100}""")
# s1=BookStore("Ali",18,"Men",70000)
# s1.info()






#m2
# class transport:
#     def __init__(self,fuel,model,max_speed,):
#         self.fuel=fuel
#         self.model=model
#         self.max_speed=max_speed
#     def get_info(self):
#         print(f"""TRANSPORT INFO:
# MODEL: {self.model}
# MAX SPEED: {self.max_speed}
# FUEL: {self.fuel}""")
# s1=transport("Electron","Kia",300)
# s1.get_info()






#m3
# class Population:
#     def __init__(self,ism,yosh,jins):
#         self.ism=ism
#         self.yosh=yosh
#         self.jins=jins
#     def __str__(self):
#         return f"""{self.ism} Yosh: {self.yosh} Jins: {self.jins}"""
    
# s1=Population("Ali",25,"Erkak")
# s2=Population("Fotima",18,"Ayol")
# s3=Population("Akrom",56,"Erkak")
# s4=Population("Dilbar",61,"Ayol")
# s5=Population("Bekmurod",19,"Erkak")

# lst=[s1,s2,s3,s4,s5]
# for i in lst:
#     if i.yosh>50:
#         if i.jins=="Erkak":
#             print(f"Ism Janob {i}")
#         else:
#             print(f"Ism Xonim {i}")
#     else:
#         print(f"ism: {i}")






#m4
# class Animal:
#     def __init__(self,name):
#         self.name=name
# class Dog(Animal):
#     def sound(self):
#         print(f"{self.name} Woof")
# s1=Dog("Max")
# s1.sound()






#m5
# class transport:
#     def __init__(self,model,year):
#         self.model=model
#         self.year=year
#     def __str__(self):
#         return f"""Model: {self.model} 
# Year: {self.year}"""
# class Car(transport):
#     def __init__(self, model, year,color):
#         super().__init__(model, year)
#         self.color=color
#     def __str__(self):
#         return f"""{super().__str__()}
#     Color: {self.color}"""
# s1=Car("Mercedec G-class",2020,"Black")
# print(s1)







#m6
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"""Name: {self.name}
# Age: {self.age}"""
# class Student(Person):
#     def __init__(self, name, age,grade):
#         super().__init__(name, age)
#         self.grade=grade
#     def __str__(self):
#         return f"""{super().__str__()}
# Grade: {self.grade}"""
# s1=Student("Ikrom",35,100)
# print(s1)





#m7
# class Building:
#     def __init__(self,address):
#         self.address=address
#     def __str__(self):
#         return f"{self.address}"
# class School(Building):
#     def __init__(self,address,student):
#         super().__init__(address)
#         self.student=student
#     def __str__(self):
#         return f"""Adress: {super().__str__()}
# Student: {self.student}"""
# s1=School("Bobur Mahallasi",34)
# print(s1)






#m8
# class Device:
#     def __init__(self,brand):
#         self.brand=brand
#     def __str__(self):
#         return f"{self.brand}"
# class Phone(Device): 
#     def __init__(self,brand,ram):
#         super().__init__(brand)
#         self.ram=ram
#     def __str__(self):
#         return f"""Brand:{super().__str__()}
# Ram: {self.ram}"""

# s1=Phone("Ipason",16)
# print(s1)






#m9
# class Food:
#     def __init__(self,name):
#         self.name=name
# class Fruit(Food):
#     def __init__(self,name,vitamin):
#         super().__init__(name)
#         self.vitamin=vitamin
#     def info(self):
#         print(f"""Name: {self.name}
# Vitamin: {self.vitamin}""")
# s1=Fruit("Apple","A") 
# s1.info()






#m10
# class Worker:
#     def __init__(self,full_name,salary):
#         self.full_name=full_name
#         self.salary=salary
#     def __str__(self):
#         return f"""full_name: {self.full_name}
# Salary: {self.salary}"""
# class Programmer(Worker):
#     def __init__(self,full_name,salary,language):
#         super().__init__(full_name,salary)
#         self.language=language
#     def __str__(self):
#         return f"""{super().__str__()}
# Language: {self.language}"""
# s1=Programmer("Azizov Vali",6000000,"Uzbek")
# s2=Programmer("Dustin Porier",10000000,"English")
# s3=Programmer("Ali Adnan",1000000000,"Arab")
# print(s1)
# print(s2)
# print(s3)






#m11
# class Vehicle:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
# class Bike(Vehicle):
#     def __init__(self,brand,speed):
#         super().__init__(brand,speed)
#         self.vazn="20 kg"
#     def info(self):
#         print(f"""Brand: {self.brand} Speed: {self.speed} Vazn: {self.vazn}""")
# s1=Bike("Utka",200)
# s1.info()
# s2=Bike("Motorbike",220)
# s2.info()
#s3=Bike("Bike",180)
#s3.info()





#m12
# class Employee:
#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
#     def __str__(self):
#         return f"""Positsiya: {self.position}
# Ism: {self.name}"""
# class Manager(Employee):
#     def __init__(self,name,position,team_size):
#         super().__init__(name,position)
#         self.team_size=team_size
#     def __str__(self):
#         return f"""{super().__str__()}
# Team_size: {self.team_size}"""
# s1=Manager("Shoxrux","Darvozabon",21)
# print(s1)








