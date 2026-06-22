#for floor
# arr=[10,20,30,40,50]
# ans=-1
# low=0
# x=5
# high=len(arr)-1
# while low<=high:
#     mid=low + (high - low)//2
#     if arr[mid]<=x:
#         ans=arr[mid]
#         low=mid+1
#     else:
#         high=mid-1
# print(ans)


#for floor and ceil

arr=[10,20,30,40,50]
floor=-1
ceil=-1
low=0
x=5
high=len(arr)-1
while low<=high:
    mid=low + (high - low)//2
    if arr[mid]==x:
        floor=arr[mid]
        ceil=floor
        
        print(floor,ceil)
    elif arr[mid]>x:
        ceil=arr[mid]
        high=mid-1
    else:
        floor=arr[mid]
        low=mid+1
print(floor,ceil)
