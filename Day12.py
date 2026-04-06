# check if string is palindrome (two pointers)
# s="racecar"
# s="hello"
# st=0
# ed=len(s)-1
# is_palindrome=True
# while(st<ed):
#     if(s[st] != s[ed]):
#         is_palindrome=False
#         break
#     st+=1
#     ed-=1
# if(is_palindrome):
#     print("true")
# else:
#     print("false")

# find pair with given sum (return true/false)
# arr=[1,2,3,4,6]
# target=6
# arr=[1,2,3,9]
# target=8
# is_found=False
# s=0
# e=len(arr)-1
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val == target):
#         is_found=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# if not is_found:
#     print("False")
# else:
#     print("True")

# count pairs with sum = target 
# arr=[1,2,3,4,3]
# target=6
# arr.sort()
# s=0
# e=len(arr)-1
# count_val=0
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val == target):
#         count_val+=1
#         s+=1
#         e-=1
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# print(count_val)

# reverse only vovel in string 
# str1="hello"
# str1=str1.lower()
# str1=list(str1)
# s=0
# e=len(str1)-1
# vow="aeiou"
# while(s<e):
#     if(str1[s] in vow and str1[e] in vow):
#         str1[s],str1[e]=str1[e],str1[s]
#         s+=1
#         e-=1
#     elif(str1[s] not in vow):
#         s+=1
#     elif(str1[e] not in vow):
#         e-=1
# print("".join(str1))