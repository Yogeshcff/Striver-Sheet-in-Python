#count occurrence


nums = [10]
target = 8
first=-1
last=-1
if not nums:
    print([0])
#for first
low=0
high=len(nums)-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        first=mid
        high=mid-1
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
#for last
low=0
high=len(nums)-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        last=mid
        low=mid+1
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
if first==-1:
    print([0])
else:
    print([last-first+1])
        
