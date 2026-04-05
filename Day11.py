# reverse array
# arr=[1,2,3,4,5]
# s=0
# e=len(arr)-1
# while(s<e):
#     arr[s],arr[e]=arr[e],arr[s]
#     s+=1
#     e-=1
# print(arr)

# function version
# def reverse_arr(arr:list):
#     if(arr==[]):
#         print("empty array")
#     else:
#         s=0
#         e=len(arr)-1
#         while(s<e):
#             arr[s],arr[e]=arr[e],arr[s]
#             s+=1
#             e-=1
#         print(arr)
# reverse_arr([2,533,213,543,1233,14])

# palindrome
# arr=[1,2,3,4,5,6,7,6,5,4,3,2,1]
# s=0
# e=len(arr)-1
# is_palindrome=True
# while(s<e):
#     if(arr[s] != arr[e]):
#         is_palindrome=False
#         break
#     s+=1
#     e-=1
# if(is_palindrome):
#     print("palindrome")
# else:
#     print("not palindrome")

# using function
# def palindrome_check(arr:list):
#     if(arr==[]):
#         return "empty list"
#     else:
#         s=0
#         e=len(arr)-1
#         is_palindrome=True
#         while(s<e):
#             if(arr[s] != arr[e]):
#                 is_palindrome=False
#                 break
#             s+=1
#             e-=1
#         if(is_palindrome):
#             print("True")
#         else:
#             print("False")
# palindrome_check([1,1,2,2,3,3,4,3,3,2,2,1,1])

# pair sum 
# arr=[1,2,3,4,5]
# target=6
# arr=[1,2,3,4,7]
# target=6
# arr=[2,3,4,8,9]
# target=10
# s=0
# e=len(arr)-1
# is_found=False
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val==target):
#         print(f"{arr[s]} + {arr[e]} = {target}")
#         is_found=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# if not is_found:
#     print("not found")

# function version
# def pair_sum(arr:list,target:int):
#     if(target==None):
#         print("empty target")
#     if(arr==[]):
#         print("empty list")
#     else:
#         s=0
#         e=len(arr)-1
#         is_found=False
#         while(s<e):
#             sum_val=arr[s]+arr[e]
#             if(sum_val == target):
#                 print(f"{arr[s]} + {arr[e]} = {target}")
#                 is_found=True
#                 break
#             elif(sum_val<target):
#                 s+=1
#             else:
#                 e-=1
#         if not is_found:
#             print("not found")
# pair_sum([1,2,3,4,5],6)
# pair_sum([1,2,3,4,7],6)
# pair_sum([2,3,4,8,9],10)