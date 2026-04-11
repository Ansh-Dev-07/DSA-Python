# 2 pointer questions
# arr=[1,2,3,4,5]
# target=8
# s=0
# e=len(arr)-1
# is_present=False
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val==target):
#         is_present=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# if(is_present):
#     print("Present")
# else:
#     print("Not Present")

# sliding window questions
# arr=[2,1,5,1,3,2]
# k=3
# window_sum=0
# for i in range(k):
#     window_sum+=arr[i]
# max_val=window_sum
# for i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]
#     if(window_sum>max_val):
#         max_val=window_sum
# print(max_val)

# 2 pointer question
# arr=[1,2,3,4,5]
# s=0
# e=len(arr)-1
# while(s<e):
#     arr[s],arr[e]=arr[e],arr[s]
#     s+=1
#     e-=1
# print(arr)

# sliding window question
# arr=[1,2,3,4,5]
# k=3
# win_count=0
# win_count+=1
# for i in range(k,len(arr)):
#     win_count+=1
# print(win_count)
# or 
# print(len(arr)-k+1)

# 2 pointer question
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
#     print("palindrome")
# else:
#     print("not palindrome")

