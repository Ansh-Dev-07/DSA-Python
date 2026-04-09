# reverse array(2 pointer)
# arr=[1,2,3,4,5]
# s=0
# e=len(arr)-1
# while(s<e):
#     arr[s],arr[e]=arr[e],arr[s]
#     s+=1
#     e-=1
# print(arr)

# function version
# def reverse_array(arr:list):
#     if(arr==[]):
#         print("empty list")
#     else:
#         s=0
#         e=len(arr)-1
#         while(s<e):
#             arr[s],arr[e]=arr[e],arr[s]
#             s+=1
#             e-=1
#         print(arr)
# reverse_array([1,2,3,4,5])

# check palindrome array
# arr=[1,2,3,2,1]
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
#     print("true")
# else:
#     print("false")

# function version
# def palindrome(arr:list):
#     if(arr==[]):
#         print("empty list")
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
#             print("true")
#         else:
#             print("false")
# palindrome([1,2,3,2,1])

# pair sum 
# arr=[1,2,3,4,5,6]
# target=7
# s=0
# e=len(arr)-1
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val == target):
#         print(f"{arr[s]} + {arr[e]} = {target}")
#         # break
#         s+=1
#         e-=1
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1

# function version
# def pair_sum_all_pairs(arr:list,target:int):
#     if(target==None):
#         print("invalid integer")
#     if(arr==[]):
#         print("empty array")
#     else:
#         s=0
#         e=len(arr)-1
#         while(s<e):
#             sum_val=arr[s]+arr[e]
#             if(sum_val == target):
#                 print(f"{arr[s]} + {arr[e]} = {target}")
#                 # break
#                 s+=1
#                 e-=1
#             elif(sum_val<target):
#                 s+=1
#             else:
#                 e-=1
# pair_sum_all_pairs([1,2,3,4,5,6],7)

# max sum subarray of size k 
# arr=[1,4,2,10,23,3,1,0,20]
# k=4
# win_sum=0
# for i in range(k):
#     win_sum+=arr[i]
# max_sum=win_sum
# for i in range(k,len(arr)):
#     win_sum=win_sum-arr[i-k]+arr[i]
#     if(win_sum>max_sum):
#         max_sum=win_sum
# print(max_sum)

# function version
# def max_sum_subarray(arr:list,k:int):
#     if(k==None):
#         print("invalid integer")
#     if(arr==[]):
#         print("empty array")
#     else:
#         win_sum=0
#         for i in range(k):
#             win_sum+=arr[i]
#         max_sum=win_sum
#         for i in range(k,len(arr)):
#             win_sum=win_sum-arr[i-k]+arr[i]
#             if(win_sum>max_sum):
#                 max_sum=win_sum
#         print(max_sum)
# max_sum_subarray([1,4,2,10,23,3,1,0,20],4)

# count windows with sum divisible by 3
# arr=[3,6,2,1,4,5]
# k=3
# win_sum=0
# win_count=0
# for i in range(k):
#     win_sum+=arr[i]
# if(win_sum%3 == 0):
#     win_count+=1
# for i in range(k,len(arr)):
#     win_sum=win_sum-arr[i-k]+arr[i]
#     if(win_sum%3==0):
#         win_count+=1
# print(win_count)

# function version
# def count_windows_divisible_by_3(arr:list,k:int):
#     if(k==None):
#         print("invalid integer")
#     if(arr==[]):
#         print("empty array")
#     else:
#         win_sum=0
#         win_count=0
#         for i in range(k):
#             win_sum+=arr[i]
#         if(win_sum%3 == 0):
#             win_count+=1
#         for i in range(k,len(arr)):
#             win_sum=win_sum-arr[i-k]+arr[i]
#             if(win_sum%3==0):
#                 win_count+=1
#         print(win_count)
# count_windows_divisible_by_3([3,6,2,1,4,5],3)