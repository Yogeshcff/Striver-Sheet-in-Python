nums = [1,2,5,9]
threshold = 6

def check(nums,mid):
    sum=0
    for i in nums:
        if i%mid==0:
            sum+=i//mid
        else:
            sum+=i//mid+1
    return sum
low=1
high=max(nums)
ans=high
while low<=high:
    mid=low+(high-low)//2
    if check(nums,mid)<=threshold:
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)
    