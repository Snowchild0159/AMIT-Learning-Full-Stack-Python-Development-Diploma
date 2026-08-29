def login_required(func) :
    def results() :
        username = input("please, enter yor username :")
        password = input("please, enter yor password :")
        
        if username == "snow" and password == "snow0159":
            func()
        else : 
            print("fuck you") 
    return results
@login_required
def sayhello() : 
    print("welcome bosee :)")      
    
    
@login_required
def sum_two_numbers() : 
    num1 = input("please enter the first number : ")    
    num2 = input("please enter the second number : ")   
    print(num1+num2) 
# sayhello()    

sum_two_numbers()         