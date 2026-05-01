# variable window 
# find minimum length subarray with sum >= target 
# arr=[2,3,1,2,4,3]
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

# window hashmap
# count number of subarrays of size k with all distinct elements. 
# arr=[1,2,1,3,4,2,3]
# k=3
# hash_map={}
# count=0
# for i in range(k):
#     curr=arr[i]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# if(len(hash_map)==k):
#     count+=1
# for i in range(k,len(arr)):
#     left=arr[i-k]
#     hash_map[left]-=1
#     if(hash_map[left]==0):
#         del hash_map[left]
#     curr=arr[i]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
#     if(len(hash_map)==k):
#         count+=1
# print(count)