# return true/false if any pair exists
# arr=[1,2,3,4,5]
# target=7
# s=0
# e=len(arr)-1
# is_exist=False
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val==target):
#         is_exist=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# print(is_exist)

# find maximum sum of subarray of size k 
# arr=[2,1,5,1,3,2]
# k=3
# win_sum=0
# for i in range(k):
#     win_sum+=arr[i]
# max_sum=win_sum
# for i in range(k,len(arr)):
#     win_sum=win_sum-arr[i-k]+arr[i]
#     if(win_sum>max_sum):
#         max_sum=win_sum
# print(max_sum)

# print all elements that appear exactly once
# arr=[1,2,2,3,3,4]
# hash_map={}
# for i in range(len(arr)):
#     curr=arr[i]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# for key in hash_map:
#     if(hash_map[key]==1):
#         print(key)