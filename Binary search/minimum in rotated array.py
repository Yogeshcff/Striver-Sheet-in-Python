nums=[5,1,2,3,4]
low=0
high=len(nums)-1
mini=float('inf')
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]<nums[high]:
        mini=min(mini,nums[mid])
        high=mid-1
    else:
        mini=min(mini,nums[mid])
        low=mid+1
print(mini)
        

    