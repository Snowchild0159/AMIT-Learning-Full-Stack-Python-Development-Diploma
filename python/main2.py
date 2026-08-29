# user_input = input("please enter your number")
# nums = user_input.split()
# nums = list(set(nums))
# int_nums = []
# for ele in nums :
#     int_nums.append(int(ele))

# int_nums.sort()

# nums.clear()

# for ele in int_nums :
#     nums.append(str(ele))
    
# result = ", ".join(nums)

# # counts = ()
# # for nums in int_nums :
# #     if nums in  counts : 
# #         counts[nums] += 1 
# #     else:
# #         counts[nums] = 1 
        
        

# print(result)

user_input = input("please enter your number : ")
nums= user_input.split()
int_nums = [int(ele) for ele in nums]
max_ele = -500
for ele in int_nums : 
    if  ele > max_ele :
         max_ele = ele 
     
    

print( f"{max_ele} is the biggest number")
# user_input = input("please enter your number : ")
# nums= user_input.split()
# int_nums = [int(ele) for ele in nums]
# min_ele = 500
# for ele in int_nums : 
#     if  ele < min_ele :
#          min_ele = ele 
     
    

# print( f"{min_ele} is the smallest number")
# user_input = input("please emter your number : ")
# nums= user_input.split()
# freq = dict()

# for num in nums : 
#     if freq.get(num) :
#         freq[num] += 1
#     else:
#         freq[num] = 1
# for ele in freq :
#     print(ele + "apears" + str(freq[ele]) + "times")
        