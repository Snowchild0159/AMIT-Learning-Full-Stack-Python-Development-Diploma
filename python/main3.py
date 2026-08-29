# def log () : 
#     print("hello world")
# log()
# x = 10 


# def say_hello() : 
#     global x 
#     x = 20 
#     print(x)
    
# print(x)
# say_hello()
# print(x)    

# def sum_numbers(*nums , commesion = 1) :
#     result = 0 
#     for ele in nums : 
#          result += ele
#     result *= commesion  
#     return result
# print(sum_numbers(1,2,3 , commesion = 7))
# def sum_numbers(*nums) :
#     result = 0 
#     for ele in nums : 
#         result += ele
#     return result
# print(sum_numbers(1,2,3))
file = open("notes.txt" , mode="r+" , encoding="utf-8")
file.write("hello snow 1")
# file = open("notes.txt" , mode="a" , encoding="utf-8")
# file.write("hello snow")