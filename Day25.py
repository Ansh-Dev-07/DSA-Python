# binary search
# find index of the target 
# arr=[1,3,5,7,9,11]
# target=7
# s=0
# e=len(arr)-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         print(mid)
#         break
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1

# return index 
# arr=[2,4,6,8,10]
# target=6
# s=0
# e=len(arr)-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         print(mid)
#         break
#     elif(arr[mid]>target):
#         e=mid-1
#     else:
#         s=mid+1

# return -1 if not found 
# arr=[1,3,5,7,9]
# target=4
# s=0
# e=len(arr)-1
# is_found=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         is_found=1
#         break
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# print(is_found)

