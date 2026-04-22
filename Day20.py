# find minimum length subarray with sum >= target 
# arr=[2,3,1,2,4,3]
# target=7
# win_sum=0
# s=0
# min_length=float('inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum>=target):
#         curr_length=i-s+1
#         if(curr_length<min_length):
#             min_length=curr_length
#         win_sum=win_sum-arr[s]
#         s+=1
# print(min_length)

# find maximum length subarray with sum<=target 
# arr=[1,2,3,4,5]
# target=11
# win_sum=0
# s=0
# max_len=float('-inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum>target):
#         win_sum=win_sum-arr[s]
#         s+=1
#     curr_len=i-s+1
#     if(curr_len>max_len):
#         max_len=curr_len
# print(max_len)

# return indices of two numbers whose sum = target 
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

# find minimun length subarray with sum >= target 
# arr=[1,4,4]
# target=4
# win_sum=0
# s=0
# min_length=float('inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum>=target):
#         curr_len=i-s+1
#         if(curr_len<min_length):
#             min_length=curr_len
#         win_sum=win_sum-arr[s]
#         s+=1
# print(min_length)

# arr=[2,3,1,2,4,3]
# target=7
# win_sum=0
# s=0
# min_len=float('inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum >= target):
#         curr_len=i-s+1
#         if(curr_len<min_len):
#             min_len=curr_len
#         win_sum-=arr[s]
#         s+=1
# print(min_len)

# find maximum length subarray with sum <= target 
# arr=[1,2,3,4,5]
# target=11
# win_sum=0
# s=0
# max_len=float('-inf')
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum > target):
#         win_sum=win_sum-arr[s]
#         s+=1
#     curr_len=i-s+1
#     if(curr_len>max_len):
#         max_len=curr_len
# print(max_len)