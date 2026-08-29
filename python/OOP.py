# class Student : 
    # def __init__(self , name , age , address):
    #     self.name = name
    #     self.__age = age
    #     self.address = address


#     def set_age(self , value) :
#         if value < 0 or value >150 : 
#             print("invalid age")
#         else : 
#             self.__age = value 
   
#     def get_age(self) :
#         return self.__age  
                     
# stu1 = Student("ahmed" , 13 , "cairo") 

# print(stu1.name)       
# print(stu1.get_age())       
# print(stu1.address)       
        
import winsound

class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

class Cat(Animal):
    def sound(self):
        winsound.Beep(1200, 200)
        winsound.Beep(1000, 200)

class Dog(Animal):
    def __init__(self, name, age, color, type):
        super().__init__(name, age, color)
        self.breed = type

    def sound(self):
        winsound.Beep(400, 300)
        winsound.Beep(500, 300)

cat = Cat("Mimi", 2, "white")
dog = Dog("Rex", 3, "brown", "wolf")

cat.sound()
dog.sound()

              