# class Student 
import winsound


def make_student(stu , name , age , address) :
    stu["name"] = name 
    stu["age"] = age 
    stu["address"] = address 
    
# stu1 = {}
# make_student(stu1, "ahmed" , 12 , "cairo" )

# print(stu1)

class Student :
    
    def __init__(self , name , age , address) :
        self.name = name 
        self.__age = age # private attribute
        self.address = address 
        
    def set_age(self , value) :
        if value < 0 or value > 150 :
            print("invalid age")
        else : 
            self.__age = value
            
    def get_age(self) :
        return self.__age
        
stu1 = Student("ahmed" , 12 , "cairo") # instantiation 
print(stu1.name)
print(stu1.get_age())
# print(stu1.__age)
print(stu1.address)
# Abstraction: hideing complexity 
# using a function is sort of abstraction

print("hello") # abstraction
# encapsulation : binding data and methods that operate on that data within one unit
# inhiretance : take properties and behaviors from another class

# Polymorphism



class Animal : 
    def __init__(self , name,  age , color):
        self.name=  name
        self.age = age 
        self.color = color
    
    def sound(self) :
        winsound.Beep(1500, 1000) 
        # raise NotImplementedError
    def walk(self) :
        print("animal walk")
        # raise NotImplementedError
        
class Dog(Animal) :
    def __init__(self, name, age, color , type):
        super().__init__(name , age , color)
        
        self.type = type 
    
    def sound(self):
        winsound.Beep(250 , 2000)
        

class Cat(Animal) :
    def sound(self):
        winsound.Beep(1250 , 2000)

d = Dog('loly' , 12 , 'blue' , 'betbool')
c = Cat('loly' , 12 , 'blue' )

d.sound()
c.sound()