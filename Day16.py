# hashing problem
# find indices
# arr=[2,7,11,15]
# target=9
# hash_map={}
# for i in range(len(arr)):
#     current=arr[i]
#     needed=target-current
#     if(needed in hash_map):
#         print(hash_map[needed],i)
#         break
#     hash_map[current]=i

# check if any pair exists
# arr=[1,2,3,4,5]
# target=10
# hash_map={}
# is_found=False
# for i in range(len(arr)):
#     current=arr[i]
#     needed=target-current
#     if(needed in hash_map):
#         is_found=True
#         break
#     hash_map[current]=i
# print(is_found)

# or using 2 pointer

# arr=[1,2,3,4,5]
# target=10
# s=0
# e=len(arr)-1
# is_found=False
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val == target):
#         is_found=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# if(not is_found):
#     print("not found")
# else:
#     print("found")

# check pair 
# arr=[3,1,4,2,5]
# target=6
# is_found=False
# hash_map={}
# for i in range(len(arr)):
#     current=arr[i]
#     needed=target-current
#     if(needed in hash_map):
#         is_found=True
#         break
#     hash_map[current]=i
# print(is_found)

# return indices
# arr=[1,2,3,4,5]
# target=9
# hash_map={}
# for i in range(len(arr)):
#     current=arr[i]
#     needed=target-current
#     if(needed in hash_map):
#         print(hash_map[needed],i)
#         break
#     hash_map[current]=i

# two sum return indices
# arr=[2,7,11,15]
# target=9
# hash_map={}
# for i in range(len(arr)):
#     curr=arr[i]
#     need=target-curr
#     if(need in hash_map):
#         print(hash_map[need],i)
#         break
#     hash_map[curr]=i

# check duplicate
# arr=[1,2,3,4,2]
# hash_map={}
# is_duplicate=False
# for i in range(len(arr)):
#     current=arr[i]
#     if(current in hash_map):
#         is_duplicate=True
#         break
#     else:
#         hash_map[current]=True
# print(is_duplicate)

# first repeating element
# arr=[1,2,3,4,2,5]
# hash_map={}
# for i in range(len(arr)):
#     current=arr[i]
#     if(current in hash_map):
#         print(current)
#         break
#     hash_map[current]=True

# frequency count
# arr=[1,2,2,3,1,4]
# hash_map={}
# for i in range(len(arr)):
#     curr=arr[i]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# print(hash_map)