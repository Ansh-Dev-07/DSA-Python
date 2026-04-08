# reverse string
# str1="python"
# str1=list(str1)
# s=0
# e=len(str1)-1
# while(s<e):
#     str1[s],str1[e]=str1[e],str1[s]
#     s+=1
#     e-=1
# print("".join(str1))

# pair sum 
# arr=[2,3,4,5,7]
# target=9
# arr=[1,2,3,9]
# target=8
# is_present=False
# s=0
# e=len(arr)-1
# while(s<e):
#     sum_val=arr[s]+arr[e]
#     if(sum_val == target):
#         is_present=True
#         break
#     elif(sum_val<target):
#         s+=1
#     else:
#         e-=1
# if(not is_present):
#     print("Not found")
# else:
#     print(is_present)

# Sliding Window
# maximum sum of subarray of size k 
# arr=[2,1,5,1,3,2]
# k=3
# window_sum=0
# for i in range(k):
#     window_sum+=arr[i]
# max_sum=window_sum
# for i in range(k,len(arr)):
#     window_sum=window_sum-arr[i-k]+arr[i]
#     if(window_sum>max_sum):
#         max_sum=window_sum
# print(max_sum)

# count subarray of size k with sum > target 
# arr=[2,1,5,1,3,2]
# k=3
# target=5
# win_sum=0
# win_count=0
# for i in range(k):
#     win_sum+=arr[i]
# if win_sum > target:
#     win_count+=1
# for i in range(k,len(arr)):
#     win_sum=win_sum-arr[i-k]+arr[i]
#     if(win_sum > target):
#         win_count+=1
# print(win_count)