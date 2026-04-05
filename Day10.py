# reverse array using two pointer 
# arr=[1,2,3,4,5,6]
# start=0
# end=len(arr)-1
# while(start<end):
#     arr[start],arr[end]=arr[end],arr[start]
#     start+=1
#     end-=1
# print(arr)

# palindrome using two pointer 
# arr=[1,2,3,4,7,3,2,1]
# start=0
# end=len(arr)-1
# is_palindrome=True
# while(start<end):
#     if(arr[start] != arr[end]):
#         is_palindrome=False
#         break
#     start+=1
#     end-=1
# if(is_palindrome):
#     print("palindrome")
# else:
#     print("not palindrome")

# pair sum (only works on sorted array)
# arr=[1,2,3,4,5,6]
# target=9
# start=0
# end=len(arr)-1
# while(start<end):
#     sum_val=arr[start]+arr[end]
#     if(sum_val == target):
#         print(f"{arr[start]} + {arr[end]} = {target}")
#         break
#     elif(sum_val<target):
#         start+=1
#     else:
#         end-=1