# count words in string 
# s="I am learning DSA"
# if(s==""):
#     print("Empty string")
# else:
#     space_count=1
#     for i in range(len(s)):
#         if(s[i] == " "):
#             space_count+=1
#     print(space_count)

# find the non-repeating character
# s="aabbcde"
# for i in range(len(s)):
#     count_val=0
#     for j in range(len(s)):
#         if(s[i]==s[j]):
#             count_val+=1
#     if(count_val==1):
#         print(s[i])
#         break

# check if two strings are anagrams
# s1="listen"
# s2="silent"
# if(len(s1)!=len(s2)):
#     print("Not Anagram")
# else:
#     is_anagram=True
#     for i in range(len(s1)):
#         count_val_s1=0
#         count_val_s2=0
#         for j in range(len(s1)):
#             if(s1[i]==s1[j]):
#                 count_val_s1+=1
#         for k in range(len(s2)):
#             if(s1[i]==s2[k]):
#                 count_val_s2+=1
#         if(count_val_s1!=count_val_s2):
#             is_anagram=False
# if(is_anagram):
#     print("anagram")
# else:
#     print("not anagram")

# move all zeroes to end 
# arr=[0,1,0,3,12]
# new_arr=[]
# for i in arr:
#     if(i!=0):
#         new_arr.append(i)
# for i in arr:
#     if(i==0):
#         new_arr.append(i)
# print(new_arr)

# find second smallest element
# arr=[4,2,7,1,3]
# small_val=float('inf')
# sec_small_val=float('inf')
# for i in arr:
#     if(i<small_val):
#         sec_small_val=small_val
#         small_val=i
#     elif(i<sec_small_val and i>small_val):
#         sec_small_val=i
# print(small_val)
# if(sec_small_val == float('inf')):
#     print("no second smallest")
# else:
#     print(sec_small_val)