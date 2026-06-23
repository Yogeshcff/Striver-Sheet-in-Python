def sra():    
    arr=[5,4,0,1,2,3]
    target=0
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return arr[mid]
        if arr[mid]>=arr[low]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1
print(sra())
        