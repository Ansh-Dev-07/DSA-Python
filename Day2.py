# find minimum
# arr=[5,2,9,1,6]
# min_val=arr[0]
# for i in range(len(arr)):
#     if(arr[i] < min_val):
#         min_val=arr[i]
# print(min_val)

# count odd number
# arr=[1,2,3,4,5,6]
# odd_val=0
# for i in arr:
#     if(i%2 != 0):
#         odd_val+=1
# print(odd_val)

# find second largest element
# arr=[3,5,1,9,7]
# large_val=float('-inf') #float('-inf') :-> here used for smallest value possible
# sec_large_val=float('-inf')
# for i in range(len(arr)):
#     if(arr[i]> large_val):
#         sec_large_val=large_val
#         large_val=arr[i]
#     elif(arr[i] > sec_large_val and arr[i] != large_val):
#         sec_large_val=arr[i]
# print(large_val)
# print(sec_large_val)

# reverse array
# arr=[1,2,3,4]
# rev_arr=[]
# for i in range(len(arr),0,-1):
#     rev_arr.append(arr[i])
# print(rev_arr)