# for(let i = 0 ; i , 10 ; i++) {
    
# }

# in 

# print("h" in "hello")
# print(1 in [ 2 , 3, 4,5])
# for i in range(0 , 10 , 1) : 
# for i in range(0 , 10 ) : 
# range( 10 ) : iterable 

# print(list(range( 10 )))
# name = 'ahmed'
# for i in name : 
# for i in range( 10 , 1 , -2 ) : 
# for i in range( 1 , 10, 3) : 
# for i in range( 10 , 0 , -1 ) : 
# for i in range( 10 , 11 , 1 ) : 
#     print("Hello" + str(i))


# for i in range(2 , 8 , 2) : 
#     print(i)


# mylist = [1 ,2 ,3 ,4 ,9 , 10]

# for i in mylist : 
#     print(i)

# name  = 'omar' 

# for c in name : 
#     print(c)


# myset = {1 , 2 , 3 , 3 , 5}

# for ele in myset : 
#     print(ele)

# mytuple= (1, 2, 3 ,4 ,5 ,6 ,5) 

# for e in mytuple :
#     print(e)

# # while 
# while condition : 
    
# password = '12345' 

# user_password = input("Please, enter your password : ")

# while password != user_password: 
#     user_password = input("Wrong password, pleas, enter it again : ")
    
# print("Welcome to your system :) ")

# user_input = input("Please, enter the numbers : ") 
# nums = user_input.split() 
# nums = list(set(nums))

# int_nums = []
# for ele in nums : 
#     int_nums.append(int(ele)) 
    
# int_nums.sort()

# # nums.clear() 
# nums = [] 

# for ele in int_nums : 
#     nums.append(str(ele))
# result = ", ".join(nums)

# print(result)


# dict 

# info = {
#     "name" : "ahmed" , 
#     "age" : 12 , 
#     "address" : {
#         "state" : "egypt" , 
#         "city" : "cairo" 
#     } , 
#     "friends" : ["ahmed" , "mohamed",  "omar"] ,
#     "driving_licence" : True 
# }

# print(info)
# 1 1 2 3
# 1 apear 2 times
# 2 apear 1 times
# 3 apear 1 times
# # print(info["first_name"])
# print(info.get("first_name" , "ahmed") )

# print(info["name"])
# print(info.get("name" , "mahmoud"))
# print(info["age"])
# print(info["address"]["city"])
# print(info["address"]["state"])
# print(info["friends"][0])
# print(info["friends"][1])
# print(info["friends"][2])
# print(info["driving_licence"])




# frequency array 
# user_input = input("Please, enter the numbers : ")
# nums=  user_input.split()  # [1,2,3,1,2,3,4]

# for ele in nums: 
#     count = 0  
#     for i in nums : 
#         if i == ele : 
#             count += 1 
#     print(ele + " apears " + str(count) + " time ")

# freq = dict()

# for num in nums:
#     if freq.get(num) : 
#         freq[num] += 1
#     else : 
#         freq[num] = 1 

# for ele in freq : 
#     print(ele + " apears " + str(freq[ele]) + " time ")
        
    
user_input = input("Please, enter the numbers : ")
nums = user_input.split() 
int_nums = [int(ele) for ele in nums  ]

min_ele = 1000000000 
for ele in int_nums : 
    if ele < min_ele : 
        min_ele = ele 
        
        
print(f"min element = {min_ele} " )
# list comprehention 

# int_nums = []

# for ele in nums : 
#     int_nums.append(int(ele)) 
    
    


