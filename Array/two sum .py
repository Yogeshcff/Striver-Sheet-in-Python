# #optimal solution for variety 1 where the goal is to return yes or no 
# # arr=[5,2,8,6,11]
# # left=0
# # n=len(arr)
# # sum=14
# # right=n-1
# # arr.sort()

# # found=False
# # while left<=right:
# #     if arr[left]+arr[right] ==sum:
# #         print("Yes")
# #         found=True
# #         break
# #     elif arr[left]+arr[right] < sum:
# #         left+=1
# #     else:
# #         right=right-1
# # if found==False:
# #     print("No")
    

# # solution using hashing

# arr=[3,-1,0,0,3]
# target=6
# premap={}
# found=False

# for i , num in enumerate(arr):
#     premap[num]=i

#     if target-num in premap:
#         found=True

# if found==False:
#     print("no")
# else:
#     print("yes")

# variety 2 with hashing
arr=[3,-1,0,0,3]
target=6
premap={}
for i , num in enumerate(arr):
    if target-num in premap:
        print(premap[target-num],i)
    premap[num]=i




