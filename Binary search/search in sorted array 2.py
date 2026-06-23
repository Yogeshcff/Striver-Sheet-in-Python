def abc():
    nums =[1]
    target=0
    low=0
    high=len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return True
        while nums[low]==nums[mid] and nums[mid]==nums[high] and len(nums)>1:
            low+=1
            high-=1
        if nums[mid]>=nums[low]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        elif nums[high]>nums[mid]:
            if nums[mid]<target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False
print(abc())