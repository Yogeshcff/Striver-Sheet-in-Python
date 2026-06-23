#brute force


# nums=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7]
# if nums[0]!=nums[1]:
#     print(nums[0])
# if nums[-1]!=nums[-2]:
#     print(nums[-1])
# for i in range (1,len(nums)-1):
#     if nums[i+1]!=nums[i] and nums[i-1]!=nums[i]:
#         print(nums[i])
        
#using xor
# xor=0
# for i in nums:
#     xor^=i
# print(xor)
    
    
#using binary search
nums=[1,1,2,2,3,3,4,4,5,6,6]
if len(nums)==1:
    print(nums[0])
    exit()
if nums[0]!=nums[1]:
    print(nums[0])
if nums[-1]!=nums[-2]:
    print(nums[-1])

    
low=1
high=len(nums)-2
while low<=high:
    mid=low+(high-low)//2
    if nums[mid-1]!=nums[mid] and nums[mid+1]!=nums[mid]:
        
        break
    if mid%2!=0:
        if nums[mid-1]==nums[mid]:
            low=mid+1
        else:
            high=mid-1
    else:
        if nums[mid-1]==nums[mid]:
            high=mid-1
        else:
            low=mid+1
print(nums[mid])
            
        
