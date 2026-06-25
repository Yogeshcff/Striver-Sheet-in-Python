def func(nums,rate):
    total_hrs=0
    for i in range (len(nums)):
        if nums[i]%rate==0:
            total_hrs+=nums[i]//rate
        else:
            total_hrs+=(nums[i]//rate +1)
    return total_hrs


    
#using binary search
deadline=10
nums=[3,6,7,11]
low=1
high=max(nums)
ans=high
while low<=high:
    mid=low+(high-low)//2
    if func(nums,mid)<=deadline:
        ans=min(mid,ans)
        high=mid-1
    else:
        low=mid+1
print(ans)
        
