# name  = input("Enter your name: ") 
# age   = input("Enter your age: ") 

# print(f"Hello, {name}! You are {age} years old.")


# user_password = input("Please, enter your passsword : ")

# if password == user_password : 
#     print("Welcome to your system :) ")
# else : 
#     print("Wrong password :( ")

# python , interactive mode 
# script mode 


# if 3 is 3 : 
#     print("hello")


# password=  "12345" 
# user_password = input("Please, enter your passsword : ")

# if password is user_password : 
#     print("Welcome to your system :) ")
# else : 
#     print("Wrong password :( ")



# x = 'ahmed' 
# y = x 

# print(x is y)
# x = 'omar'
# print(x is y)

# print(x)
# print(y)


# # (True , False , None)

# x = 'ahmed ali' 
# y = 'ahmed ali' 
# print(x is y)


# string methods in python 
# import string
# string are immutable ()
# x = 'hellO world'
# x = x.upper()
# x = x.lower()
# x = x.title()
# x = x.capitalize()
# x = x.casefold()

# x = 'hellOworld'
# x = '324563.3'
# x = 'Hell oworld'
# print(x[: : -1])
# x[0] = "M"
# print(x)
# print(x.rfind("o"))
# print(x.find("o"))
# print(x.rindex("o"))
# print(x.split("l"))
# print("".join(sorted(x)))
# print(x.index("z"))
# print(x.count("O"))
# print(x.islower())
# print(x.isupper())
# print(x.isalpha())
# print(x.isnumeric())
# print(x.isdecimal())
# print(x.isdigit())
# print(x.isalnum())
# print(x.istitle())
# print(x.isidentifier())
# print(x.isspace())
# print(x.islower()) 

# name1 = input("Enter your name : ") # ahmed mohamed
# name2= input("Enter your name : ") # omar mohamed

# name1_names = name1.split() # ['ahmed' , 'mohamed']
# name2_names = name2.split() # ['omar' , 'moahmed']
# if name1_names[1].upper()  == name2_names[1].upper() :
#     print("may be brothere :) ")
# else : 
#     print("can't be brothers")

# programming
# progamin
# lists


# x = ["ahmed" , "mohamed", 'ahmed' , "hamada"] 
# x.append('saeed')
# # x.pop(1)
# # x.remove("ahmed")
# # x.clear()
# # print(x.count("ahmed"))
# print(x.index("mohamed"))
# # print(x.extend(['ali' , 'sameh']))

# # print(x + ['ali' , 'sameh'])
# # x.sort(reverse=True)
# # x.reverse()

# print(x[:: -1] )

# tuple  : immutable 
# x = ('ahmed' , 'mohamed' , 'omar')
# # x[0] = "hossam"
# print(x.count("ahemd"))
# print(x.index("ahmed"))


# # set 
# # remove doublecates
# x = {"ahmed" , "mohamed" , "hossam" , "ahmed" }
# # print(x[0])
# x.add("essam")
# # x.remove("essam")
# x.pop()
# print(x)
# # print(x)
# list 
# set
# tuple
x = [1,2,3,4,5 , 5]
# print(tuple(x))

x = list(set(x))
print(x)