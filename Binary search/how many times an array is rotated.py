nums=[4,5,6,7,0,1,2,3]
low=0
high=len(nums)-1
mini=float('inf')
index=0
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]<mini:
            mini=nums[mid]
            index=mid
    if nums[mid]<nums[high]:
        high=mid-1
    else:
        low=mid+1
print(index)
        

    