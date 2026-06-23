def sra():    
    arr=[5,1,3]
    target=3
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        if arr[mid]>=arr[low]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        if arr[high]>arr[mid]:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
print(sra())
        