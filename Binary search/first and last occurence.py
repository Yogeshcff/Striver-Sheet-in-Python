#brute force

# nums=[2,4,6,8,8,8,8,8,11,13]
# f=-1
# l=-1
# x=8
# for i in range (len(nums)):
#     if nums[i]==x:
#         l=i
#         if f==-1:
#             f=i
# print(f,l)


#binary search method

# nums=[2,8,8,8,8,8,8,8,8,8]
# first=-1
# last=-1
# x=10
# low=0
# high=len(nums)-1
# while low<=high:
#     mid=low+(high-low)//2
#     if nums[mid]==x:
#         first=mid
#         last=mid
#         break
#     elif nums[mid]>x:
#         high=mid-1
#     else:
#         low=mid+1
# if first!=-1:
#     j=mid
#     i=mid
#     while  j>=0 and nums[j]==x  :
#         first=j
#         j-=1
#     while i<len(nums) and nums[i]==x:
#         last=i
#         i+=1
#     print(first,last)
# else:
#     print(first,last)
        


#using upper and lower bound

nums = [5,7,7,8,8,10]
target = 8
first=-1
last=-1
if not nums:
    print([-1,-1])
#for first
low=0
high=len(nums)-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        first=mid
        last=mid
        high=mid-1
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
#for last
low=0
high=len(nums)-1
while low<=high:
    mid=low+(high-low)//2
    if nums[mid]==target:
        last=mid
        low=mid+1
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1

if first==-1:
    print([-1,-1])
print([first,last])
        
