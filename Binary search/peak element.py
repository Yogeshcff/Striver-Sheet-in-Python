# #finding peak element using brute force

# nums=[1,2,3,4,5,6,7,8,5,1]
# if len(nums)==1:
#     print(nums[0])
#     exit()
# if nums[0]>nums[1]:
#     print(nums[0])
#     exit()
# if nums[-1]>nums[-2]:
#     print(nums[-1])
#     exit()
# for i in range (1, len(nums)-1):
#     if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
#         print(nums[i])
        
        
#assuming array has onle one peak

nums=[1,2,1,3,2]
if len(nums)==1:
    print(nums[0])
    exit()
if nums[0]>nums[1]:
    print(nums[0])
    exit()
if nums[-1]>nums[-2]:
    print(nums[-1])
    exit()
low=1
high=len(nums)-2
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        
        break
    if nums[mid]>nums[mid-1]:
        low=mid+1
    else:
        high=mid-1
print(mid)