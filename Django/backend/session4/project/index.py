# # decorators 


# # function (function) => function 


# # def print_before(f) :
    
# #     def result() :
# #         print("hello worlf")
# #         f()
        
# #     return result

# # @print_before
# # def sum_two_numbers():    
# #     print("Hello from sum two numbers")

# # # sum_two_numbers = print_before(sum_two_numbers)
# # sum_two_numbers()


# def login_required(func) :
#     def result () :
#         username = input("please, enter your username : ")
#         password = input("please, enter your password : ")
        
#         if username == "admin" and password == "admin" : 
#             func()
#         else : 
#             print('You aree not authenticated')
#     return result 

# @login_required
# def say_hello() :
#     print("WElcome to your system :)")
 

# @login_required
# def sum_two_numbers() : 
#     num1 = input("Please, enter the first number : ")
#     num2 = input("please, enter the second number : ") 
#     print(num1 + num2 )


# sum_two_numbers()

import psycopg2

conn = psycopg2.connect(
    dbname = "pythonconn" ,
    host = "localhost" ,
    port = "5432" ,
    user = "postgres" ,
    password = "@2bdelfatta77"
)

cursor = conn.cursor()


cursor.execute("select * from student ;")

print(cursor.fetchall())