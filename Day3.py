# find minimum
# arr=[4,2,7,1,9]
# min_val=float('inf')
# for i in arr:
#     if(i<min_val):
#         min_val=i
# print(min_val)

# count positive number
# arr=[-1,2,3,-4,5]
# pos_count=0
# for i in arr:
#     if(i>0):
#         pos_count+=1
# print(pos_count)

# check if array is sorted
# arr=[1,2,3,4,5]
# arr=[1,3,2,4]
# is_sorted=True
# for i in range(len(arr)-1):
#     if(arr[i]>arr[i+1]):
#         is_sorted=False
#         break
# print(is_sorted)

# find the sum of even numbers
# arr=[1,2,3,4,5,6]
# even_sum=0
# for i in arr:
#     if(i%2==0):
#         even_sum+=i
# print(even_sum)

# find largest and second largest
# arr=[3,5,1,9,7]
# large_val=float('-inf')
# sec_large_val=float('-inf')
# for i in arr:
#     if(i>large_val):
#         sec_large_val=large_val
#         large_val=i
#     elif(sec_large_val < i and large_val != i):
#         sec_large_val=i
# print(large_val)
# print(sec_large_val)