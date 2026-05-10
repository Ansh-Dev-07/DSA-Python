# return index 
# arr=[1,3,5,6]
# target=5
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

# insert position
# arr=[1,3,5,6]
# target=2
# s=0
# e=len(arr)-1
# ans=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         ans=mid
#         break
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# if(ans != -1):
#     print(ans)
# else:
#     print(s)

# count occurrences
# arr=[1,2,2,2,3]
# target=2
# s=0
# e=len(arr)-1
# first=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         first=mid
#         e=mid-1
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# s=0
# e=len(arr)-1
# last=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         last=mid
#         s=mid+1
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# if(first == -1):
#     print(0)
# else:
#     print(last-first+1)

# insert position if target = 5
# arr=[1,2,2,3,3,3,4]
# target=5
# s=0
# e=len(arr)-1
# ans=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         ans=mid
#         break
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# if(ans != -1):
#     print(ans)
# else:
#     print(s)

# count occurrences
# arr=[1,2,2,3,3,3,4]
# target=3
# s=0
# e=len(arr)-1
# first=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         first=mid
#         e=mid-1
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# s=0
# e=len(arr)-1
# last=-1
# while(s<=e):
#     mid=(s+e)//2
#     if(arr[mid]==target):
#         last=mid
#         s=mid+1
#     elif(arr[mid]<target):
#         s=mid+1
#     else:
#         e=mid-1
# if(first == -1):
#     print(0)
# else:
#     print(last-first+1)