# check if element exists
# arr=[1,3,5,7,9]
# key=5
# is_present=False
# for i in range(len(arr)):
#     if(arr[i]==key):
#         is_present=True
#         print(f"{arr[i]} found at {i}")
#         break
# print(is_present)

# count frequency of a number
# arr=[1,2,2,3,2,4]
# key=2
# freq_count=0
# for i in arr:
#     if(i==key):
#         freq_count+=1
# print(freq_count)

# find first occurence index 
# arr=[4,6,2,6,7]
# key=6
# is_present=False
# for i in range(len(arr)):
#     if(arr[i]==key):
#         is_present=True
#         print(i)
#         break
# if not is_present:
#     print("Not Found")

# find last occurrence index 
# arr=[4,6,2,6,7]
# key=6
# is_present=False
# for i in range(len(arr)-1,-1,-1):
#     if(arr[i]==key):
#         is_present=True
#         print(i)
#         break
# if not is_present:
#     print("Not Found")

# check if array contains duplicate
# arr=[1,2,3,4,2]
# is_duplicate=False
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if(arr[i]==arr[j]):
#             is_duplicate=True
#             break
#     if is_duplicate:
#         break
# if not is_duplicate:
#     print("No Duplicate Found")
# else:
#     print(is_duplicate)