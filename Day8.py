# reverse array (in-place) {two pointer}
# arr=[1,2,3,4,5]
# start=0
# end=len(arr)-1
# while(start<end):
#     arr[start],arr[end]=arr[end],arr[start]
#     start+=1
#     end-=1
# print(arr)

# check if array is palindrome
# arr=[1,2,3,2,1]
# arr=[1,2,3,4]
# first=0
# last=len(arr)-1
# is_palindrome=True
# while(first<last):
#     if(arr[first]!=arr[last]):
#         is_palindrome=False
#         break
#     first+=1
#     last-=1
# if(is_palindrome):
#     print("palindrome")
# else:
#     print("not palindrome")

# remove duplicate
# arr=[1,1,2,2,3]
# new_arr=[]
# for i in range(len(arr)):
#     if(arr[i] not in new_arr):
#         new_arr.append(arr[i])
# print(new_arr)