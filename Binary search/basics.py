# def binarysearch(arr,target):
    
#     n=len(arr)
#     target=13
#     low=0
#     high=n-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]>target:
#             high=mid-1
#         elif arr[mid]<target:
#             low=mid+1
#         else:
#             return mid
#     return -1
# print(binarysearch([2,4,6,7,9,11,18,19],13))

def bs(nums,low,high,target):
    if low>high:
        return -1
    mid=low+(high-low)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target :
        return bs(nums,mid+1,high,target)
    else:
        return bs(nums,low,mid-1,target)
nums= [2,4,6,7,9,11,18,19]
n=len(nums)-1  
print(bs(nums,0,n,0))