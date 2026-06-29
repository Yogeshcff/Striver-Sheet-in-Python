#brute force using linear search

# arr=[1,2,3,3,7,8,9,9,9,11]
# x=20
# for i in range (len(arr)):
#     if arr[i]>=x:
#         print(i)
#         break
# else:
#     print(len(arr))


#using binary search lower bound

# arr=[1,2,3,3,7,8,9,9,9,11]
# x=3
# ans=10
# low=0
# high=len(arr)-1
# while low <=high:
#     mid=low+(high-low)//2
#     if arr[mid]>=x:
#         ans=mid
#         high=mid-1
#     elif arr[mid]<x:
#         low=mid+1
# print(ans)
    
    
#upper bound 
arr=[2,3,6,7,8,8,11,11,11,12]
x=1
ans=10
low=0
high=len(arr)-1
while low <=high:
    mid=low+(high-low)//2
    if arr[mid]<=x:
        low=mid+1
    else:
        ans=mid
        high=mid-1
print(ans)

