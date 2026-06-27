def check(nums,maxsum,k):
    current_sum=0
    subarray=1
    for i in nums:
        if current_sum+i>maxsum:
            subarray+=1
            current_sum=i
        else:
            current_sum+=i
    return subarray<=k
nums = [7,2,5,10,8] 
k = 2
low=max(nums)
high=sum(nums)
while low<=high:
    mid=low+(high-low)//2
    if check(nums,mid,k):
        high=mid-1
    else:
        low=mid+1
print(low)