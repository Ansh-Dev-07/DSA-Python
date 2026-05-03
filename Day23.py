# prefix array
# build prefix array and find sum from index 1 to 3
# arr=[1,3,2,5]
# prefix=[0]*len(arr)
# prefix[0]=arr[0]
# for i in range(1,len(arr)):
#     prefix[i]=prefix[i-1]+arr[i]
# print(prefix)
# l=1
# r=3
# if(l==0):
#     answer=prefix[r]
# else:
#     answer=prefix[r]-prefix[l-1]
# print(answer)

# count subarray with sum = target 
# arr=[1,2,3]
# arr=[1,1,1]
# arr=[3,1,2,4]
# arr=[1,2,1,2,1]
# t=3
# prefix_sum=0
# hash_map={}
# count=0
# for i in range(len(arr)):
#     prefix_sum+=arr[i]
#     if(prefix_sum == t):
#         count+=1
#     need=prefix_sum-t
#     if(need in hash_map):
#         count+=hash_map[need]
#     if(prefix_sum in hash_map):
#         hash_map[prefix_sum]+=1
#     else:
#         hash_map[prefix_sum]=1
# print(hash_map)
# print(count)
# print(prefix_sum)

# practice set :-
# arr=[2,1,1,2]
# t=3
# arr=[1,1,1]
# t=1
# arr=[3,4,7,2,-3,1,4,2]
# t=7
# prefix_sum=0
# hash_map={}
# count=0
# for i in range(len(arr)):
#     prefix_sum+=arr[i]
#     if(prefix_sum == t):
#         count+=1
#     need=prefix_sum-t
#     if(need in hash_map):
#         count+=hash_map[need]
#     if(prefix_sum in hash_map):
#         hash_map[prefix_sum]+=1
#     else:
#         hash_map[prefix_sum]=1
# print(hash_map)
# print(count)
# print(prefix_sum)