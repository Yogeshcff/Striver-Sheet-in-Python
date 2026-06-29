#Its asking for lower bound


arr=[1,2,3,3,7,8,9,9,9,11]
x=3
ans=10
low=0
high=len(arr)-1
while low <=high:
    mid=low+(high-low)//2
    if arr[mid]>=x:
        ans=mid
        high=mid-1
    elif arr[mid]<x:
        low=mid+1
print(ans)