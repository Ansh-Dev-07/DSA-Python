# count number of pairs
# arr=[1,1,1,1]
# target=2
# hash_map={}
# count_val=0
# for i in range(len(arr)):
#     curr=arr[i]
#     need=target-curr
#     if(need in hash_map):
#         count_val=count_val+hash_map[curr]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# print(count_val)

# find any subarray with sum = target (not fixed size)
# arr=[2,1,5,2,3,2]
# target=7
# s=0
# win_sum=0
# is_found=False
# for i in range(len(arr)):
#     win_sum+=arr[i]
#     while(win_sum>target):
#         win_sum=win_sum - arr[s]
#         s+=1
#     if(win_sum == target):
#         is_found=True
#         break
# print(is_found)

# find first non-repeating element
# arr=[1,2,3,1,2,3,4]
# hash_map={} 
# for i in range(len(arr)):
#     curr=arr[i]
#     if(curr in hash_map):
#         hash_map[curr]+=1
#     else:
#         hash_map[curr]=1
# for i in hash_map:
#     if(hash_map[i]<2):
#         print(i)
#         break

# or we can use 

# for num in arr:
#     if(hash_map[num]==1):
#         print(num)
#         break

# count number of subarray of size 2
# arr=[1,2,3,4,5]
# k=2
# win_sum=0
# for i in range(k):
#     win_sum+=arr[i]
# win_count=1
# for i in range(k,len(arr)):
#     win_sum=win_sum-arr[i-k]+arr[i]
#     win_count+=1
# print(win_count)