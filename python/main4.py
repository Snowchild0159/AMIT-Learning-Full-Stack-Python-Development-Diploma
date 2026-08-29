class Student : 
    def __init__(self , age , name , GPA):
        self.age = age 
        self.name = name
        self.GPA = GPA
        
    @property
    def name(self) :
        return self.__name
    @name.setter
    def name(self, value) : 
        value = str(value)
        if len (value) > 5 :
            self.__name = value
        else : 
            raise ValueError ("name must be more than 5 chars")           
    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self, value) : 
        value = int(value)
        if value > 0 and value < 150  :
            self.__age = value
        else : 
            raise ValueError ("age must be between 0 and 150")           
    @property
    def GPA(self) :
        return self.__GPA
    @GPA.setter
    def GPA(self, value) : 
        value = int(value)
        if value > 2 :
            self.__GPA = value
        else : 
            raise ValueError ("you faild at this year")           
        
stu1 = Student(190, 'Mohammed', 1)
stu1.age = 190
print(stu1.age, stu1.name, stu1.GPA)