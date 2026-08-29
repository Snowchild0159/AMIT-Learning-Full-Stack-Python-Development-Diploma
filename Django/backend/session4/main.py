"""
hello from main

"""

# functions in python 
# function functionname() {
    
# }

# def function_name() : 
#     pass 


# def log() :
#     print("Hello World")
    
    
# log()

# def sum_numbers(num1 , num2) : 
#     result = num1 + num2 
    
#     return result 

# sum_numbers(2,3)
# print(result)
# output = sum_numbers(2,3)

# print(output)

# variable scopping 

# builtin scope 

# print()
# type()
# len()

# # name=  "ahmed"
# nums = [1,2,3,4]
# print(len(nums))


# globla scope 

x = 10 

# def say_hello() : 
#     global x
#     x = 20
#     print(x)
    
# print(x) 
# say_hello()
# print(x)


# def sum_numbers(num1 = 0  , num2 = 0 , num3 = 0 , num4 = 0) :
#     result = num1 + num2  + num3 + num4
# #     return result
# def sum_numbers(*nums , commesion =1) :
    
#     result = 0 
    
#     for ele in nums : 
#         result += ele
        
#     result *= commesion
#     return result

# print(sum_numbers(1,2,3 , 4 , 5 , 6 , 7 ,commesion= 10 ) )
    
    
# print("ahmed" , "mohamed" , "ali" , "*")




# file = open("notes.txt" , mode="a" , encoding="utf-8")
# file = open("notes.txt" , mode="r+" , encoding="utf-8")

# file.write("hello brother ")
# file.close()
# while True : 
#     pass


# file = open("notes2.txt" , mode="w" , encoding="utf-8")


# with open("notes.txt" , mode="r+" , encoding="utf-8") as file : 
#     file.write("hello sis")
    
# while True : 
#     pass 


# import index

# # print(index.y)
# # print(index.say_hello())



# from index import y

# say_hello()
# print(y)

# import index 

# print(index.__doc__)
# print(index.__file__)
# print(index.__name__)

# print(__doc__)
# print(__name__)


def day_hello() :
    """
    Docstring for day_hello
    """
    
    print('Hello')
    
print(day_hello.__doc__)