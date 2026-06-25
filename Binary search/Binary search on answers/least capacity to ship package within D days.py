weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
def totaldays(weights,capacity):
    day=1
    load=0
    for i in weights:
        if load+i>capacity:
            day+=1
            load=i
        else:
            load+=i
    return day

        
low=max(weights)
high=sum(weights)
while low<=high:
    mid=low+(high-low)//2
    if totaldays(weights,mid)<=days:
        high=mid-1
    else:
        low=mid+1
print(low)
        
        