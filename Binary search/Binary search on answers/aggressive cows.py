n = 4
cow = 4
arr = [79,74,57,22]
arr.sort()

def check(arr,dist,cow):
    countcow=1
    lastcow=arr[0]
    for i in range (1,n):
        if arr[i]-lastcow>=dist:
            countcow+=1
            lastcow=arr[i]
            if countcow>=cow:
                return True
        
    return False
low=1
high=max(arr)-min(arr)
ans=-1
while low<=high:
    mid=low+(high-low)//2
    if check(arr,mid,cow)==True:
        
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(high)
    