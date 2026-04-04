# reverse array
# arr=[1,2,3,4,5,6]
# st=0
# ed=len(arr)-1
# while(st<ed):
#     arr[st],arr[ed]=arr[ed],arr[st]
#     st+=1
#     ed-=1
# print(arr)

# check palindrome
# arr=[1,2,3,3,2,1]
# st=0
# ed=len(arr)-1
# is_palindrome=True
# while(st<ed):
#     if(arr[st] != arr[ed]):
#         is_palindrome=False
#         break
#     st+=1
#     ed-=1
# if(is_palindrome):
#     print("palindrome")
# else:
#     print("not palindrome")

# check if sorted 
# arr=[1,2,3,4,5]
# arr=[1,3,2,4]
# is_sorted=True
# for i in range(len(arr)-1):
#     if(arr[i]>arr[i+1]):
#         is_sorted=False
#         break
# if(is_sorted):
#     print("sorted")
# else:
#     print("not sorted")

# pair sum 
# arr=[1,2,3,4,7]
# target=5
# st=0
# ed=len(arr)-1
# while(st<ed):
#     sum_val=arr[st]+arr[ed]
#     if(sum_val == target):
#         print(arr[st], "+", arr[ed], "=", target)
#         break
#     elif(sum_val < target):
#         st+=1
#     else:
#         ed-=1