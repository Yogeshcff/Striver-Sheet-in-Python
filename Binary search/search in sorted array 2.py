def abc():
    nums =[1,0,1,1,1]
    target=0
    low=0
    high=len(nums)-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return True
        if nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue
        if nums[mid]>=nums[low]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
                
                 
    return False
print(abc())