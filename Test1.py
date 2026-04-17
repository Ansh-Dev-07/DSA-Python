# count number of pairs.
# arr=[2,2,2,2]
# target=4
# hash_map={}
# count_val=0
# for i in range(len(arr)):
#     curr=arr[i]
#     need=target-curr
#     if(need in hash_map):
#         count_val=count_val+hash_map[need]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# print(count_val)

# return true/false is any pair existes 
# arr=[1,2,3,4,5]
# target=11
# s=0
# e=len(arr)-1
# is_found=False
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val==target):
#         is_found=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# print(is_found)

# count number of subarray of size k with all distinct elements
# arr=[1,2,1,3,4,2,3]
# k=4
# hash_map={}
# count_val=0
# for i in range(k):
#     curr=arr[i]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# if(len(hash_map)==k):
#     count_val+=1
# for i in range(k,len(arr)):
#     prev=arr[i-k]
#     hash_map[prev]-=1
#     if(hash_map[prev]==0):
#         del hash_map[prev]
#     newel=arr[i]
#     if(newel in hash_map):
#         hash_map[newel]+=1
#     else:
#         hash_map[newel]=1
#     if(len(hash_map)==k):
#         count_val+=1
# print(count_val)

# find length of smallest subarray with sum >= target 
# arr=[4,2,2,7,8,1,2,8,1,0]
# target=8
# win_sum=0
# s=0
# min_len=float('inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum>=target):
#         curr_len=i-s+1
#         if(curr_len<min_len):
#             min_len=curr_len
#         win_sum=win_sum-arr[s]
#         s+=1
# print(min_len)

# count number of subarrays whose sum is even 
# arr=[1,2,3,4,5]
# win_sum=0
# count_val=0
# even_c=1 #because previous element which is 0 is even
# odd_c=0
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     if(win_sum%2==0):
#         count_val=count_val+even_c
#         even_c+=1
#     else:
#         count_val=count_val+odd_c
#         odd_c+=1
# print(count_val)