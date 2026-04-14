# count number of pairs with sum = target
# arr=[1,2,3,4,6]
# target=6
# s=0
# e=len(arr)-1
# count_val=0
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val == target):
#         count_val+=1
#         s+=1
#         e-=1
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# print(count_val)

# find if there exists any subarray of size 3 with sum = 9
# arr=[1,2,3,4,5]
# k=3
# target=9
# win_sum=0
# for i in range(k):
#     win_sum+=arr[i]
# if(win_sum==target):
#     print("present")
# for i in range(k,len(arr)):
#     win_sum=win_sum-arr[i-k]+arr[i]
#     if(win_sum == target):
#         print("present")
#         break

# find element with highest frequency
# arr=[1,2,2,3,3,3]
# hash_map={}
# for i in range(len(arr)):
#     current=arr[i]
#     if(current in hash_map):
#         hash_map[current]+=1
#     else:
#         hash_map[current]=1
# max_freq=0
# max_elem=None
# for current in hash_map:
#     if(hash_map[current]>max_freq):
#         max_freq=hash_map[current]
#         max_elem=current
# print(max_elem)

# find maximum sum of any subarray of size k 
# arr=[2,1,5,2,3,2]
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

# find majority element (appears more then n/2 times)
# arr=[3,3,4,2,4,4,2,4,4]
# hash_map={}
# for i in range(len(arr)):
#     now=arr[i]
#     if(now in hash_map):
#         hash_map[now]+=1
#     else:
#         hash_map[now]=1
# n=len(arr)
# for now in hash_map:
#     if(hash_map[now]>n//2):
#         print(now)
#         break