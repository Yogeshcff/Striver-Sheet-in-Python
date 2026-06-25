#brute force to find kth missing number


arr = [1,2,3,4]
k = 2
# miss=0
# for i in range (1,max(arr)+k+1):
#     if i not in arr:
#         miss+=1
#         if miss==k:
#             print(i)
#             break

#using binary search
low=0
high=len(arr)-1
while low<=high:
    mid=low+(high-low)//2
    miss=arr[mid]-(mid+1)
    if miss<k:
        low=mid+1
    else:
        high=mid-1
print(high+1+k)
        