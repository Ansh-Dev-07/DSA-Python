# kadane's algorithm
# find max sum of any subarray
# arr=[-2,1,-3,4,-1,2,1,-5,4]
# curr_sum=0
# max_sum=float('-inf')
# for i in range(len(arr)):
#     curr_sum+=arr[i]
#     if(curr_sum>max_sum):
#         max_sum=curr_sum
#     if(curr_sum<0):
#         curr_sum=0
# print(max_sum)

# find maximum sum of any subarray
# arr=[1,2,3,-2,5]
# curr_sum=0
# max_sum=float('-inf')
# for i in range(len(arr)):
#     curr_sum+=arr[i]
#     if(curr_sum>max_sum):
#         max_sum=curr_sum
#     if(curr_sum<0):
#         curr_sum=0
# print(max_sum)

# find max sum 
# arr=[-2,-3,4,-1,-2,1,5,-3]
# max_sum=float('-inf')
# curr_sum=0
# for i in range(len(arr)):
#     curr_sum+=arr[i]
#     if(curr_sum>max_sum):
#         max_sum=curr_sum
#     if(curr_sum<0):
#         curr_sum=0
# print(max_sum)

# find minimum sum 
# arr=[3,-4,2,-3,-1,7,-5]
# curr_sum=0
# min_sum=float('inf')
# for i in range(len(arr)):
#     curr_sum+=arr[i]
#     if(curr_sum<min_sum):
#         min_sum=curr_sum
#     if(curr_sum>0):
#         curr_sum=0
# print(min_sum)