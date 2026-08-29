# any interaction with user : input, print 


# pip install virtualenv
# virtaulenv myenv 
# .\myenv\Scripts\activate
# pip install psycopg-binary

from controllers import validate_student , valide_id , delete_id
from utils import error_messages

def get_student_by_id(f):
    def wrapper() : 
        id = input("Please , enter student Id : ")
        status , output = valide_id(id) 
        if status is True : 
            f(output)
        else : 
            print("Please, enter a valid id :)")
    return wrapper
    
    
def log_error(error) :
    if str(type(error)) == "<class 'str'>":
        print(f"error happen {error}") 
    else : 
        print("Please, solve these errors : ")
        
        for error in error : 
            print(error_messages[error])    
    
def create_student() : 
    name = input("please, enter student name : ")
    age = input("please, enter student age : ")
    address = input("please, enter student address : ")
    phone_number = input("please, enter student phone number : ")
    success , output = validate_student(name , age,  address , phone_number)  # ["age"]
     
    if success : 
        print(f"Stduent Saved successfully with id= {output} :) ")
    else :
        log_error(output)
        
            
@get_student_by_id
def update_student(student):

    name= input(f"You want to change {student['name'] } to : ")
    age= input(f"You want to change {student['age'] } to : ")
    address= input(f"You want to change {student['address'] } to : ")
    phone_number= input(f"You want to change {student['phone_number'] } to : ")
    success , output = validate_student(name , age,  address , phone_number , student) 
    if success : 
        print("Student updated sucessfully :) ")
    else : 
        log_error(output)
  
@get_student_by_id
def read_student(student) :
    print_student(student)

@get_student_by_id 
def delete_student(student) : 
    delete_id(student)
    print(f"Stduent with id {id} deleted successfully :) ")

    
    

def print_student(stduent) :
    for key in stduent : 
        print(f"student {key} : {stduent[key]} " )
        

def list_stduents() :
    from models import data 
    for student in data : 
        print_student(student)   
        print("\n\n******************************************************\n\n")
def log_system_functions(): 
    print("""Here's what you can do in our system 
        1. Create Student
        2. Read Student
        3. Update Student 
        4. Delete Stduent
        5. List Stduents
        6. Close 
        """)
    choice = input("Enter your choice : ")
    return choice
def start() :
    print("Welcome to our system") 
    while True : 
        choice = log_system_functions()
        
        if choice == "1" : 
            create_student() 
        elif choice == "2" : 
            read_student()
        elif choice == "3" : 
            update_student() 
        elif choice == "4" : 
            delete_student() 
        elif choice == "5" : 
            list_stduents() 
        elif choice == "6" :
            print("Good Bye")
            break
            
        else: 
            print("Wrong input, please enter valid choice :) ") 
        
    