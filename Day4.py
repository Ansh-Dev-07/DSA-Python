# difference between max and min
# arr=[3,7,2,9,5]
# max_val=float('-inf')
# min_val=float('inf')
# for i in range(len(arr)):
#     if(arr[i]>max_val):
#         max_val=arr[i]
#     if(arr[i]<min_val):
#         min_val=arr[i]
# print(max_val)
# print(min_val)
# diff_val=max_val-min_val
# print(f"The difference between max value and min value is : {diff_val}")

# count element greater than average
# arr=[1,2,3,4,5]
# sum_val=0
# for i in arr:
#     sum_val+=i
# avg_val=sum_val/len(arr)
# large_than_avg_val=0
# for i in arr:
#     if(i>avg_val):
#         large_than_avg_val+=1
# print(large_than_avg_val)

# smallest even number
# arr=[5,2,8,1,3]
# small_even_val=float('inf')
# for i in arr:
#     if(i<small_even_val and i%2==0):
#         small_even_val=i
# if(small_even_val==float('inf')):
#     print("No even number found in the array")
# else:
#     print(small_even_val)

# check if all elements are positive
# arr=[1,2,3,4]
# arr=[1,-2,3]
# is_positive=True
# for i in arr:
#     if(i<0):
#         is_positive=False
#         break
# print(is_positive)

# sum of elements at even index
# arr=[1,2,3,4,5]
# even_index_sum=0
# for i in range(len(arr)):
#     if(i%2==0):
#         even_index_sum+=arr[i]
# print(even_index_sum)