# variable window 
# find minimum length subarray with sum >= target 
# arr=[3,1,4,1,5]
# target=7
# win_sum=0
# s=0
# min_len=float('inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum>=target):
#         curr_len=i-s+1
#         if(curr_len<min_len):
#             min_len=curr_len
#         win_sum-=arr[s]
#         s+=1
# print(min_len)

# hashing
# return true if pair exists
# arr=[1,2,3,4,5,6]
# target=10
# hash_map={}
# is_exists=False
# for i in range(len(arr)):
#     curr=arr[i]
#     need=target-curr
#     if(need in hash_map):
#         is_exists=True
#         break
#     hash_map[curr]=1
# print(is_exists)

# hashing
# return indices
# arr=[1,2,3,4,5,6]
# target=10
# hash_map={}
# for i in range(len(arr)):
#     curr=arr[i]
#     need=target-curr
#     if(need in hash_map):
#         print(hash_map[need],i)
#         break
#     hash_map[curr]=i
