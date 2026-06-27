nums = [1,2,3,4,5]
m = 2

def check(nums,maxpage,m):
    current_page=0
    student=1
    for i in nums:
        if current_page+i>maxpage:
            student+=1
            current_page=i
        else:
            current_page+=i
    return student<=m
# print(check(nums,49,m))  
low=max(nums)
high=sum(nums)
while high>=low:
    mid=low+(high-low)//2
    if check(nums,mid,m):
        high=mid-1
    else:
        low=mid+1
print(low)
            
    