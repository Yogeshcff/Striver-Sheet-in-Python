# using 1 pass but extra space

# arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
# c0 = 0
# c1 = 0
# c2 = 0
# for i in arr:
#     if i == 0:
#         c0 += 1
#     elif i == 1:
#         c1 += 1
#     else:
#         c2 += 1
# ans = [0]*c0+[1]*c1+[2]*c2
# print(ans)


# using 2 pass but no extra space
# nums=[0,0,1,1,2,1,0,1,2,0]
# c0 = 0
# c1 = 0
# c2 = 0
# for i in nums:
#     if i == 0:
#         c0 += 1
#     elif i == 1:
#         c1 += 1
#     else:
#         c2 += 1
# for x in range(c0):
#     nums[x] = 0
# for y in range (c0, c0+c1):
#     nums[y] = 1
# for z in range (c0+c1, c0+c1+c2):
#     nums[z] = 2
# print(nums)

# most optimal solution dutch national flag algorithm
arr = [0, 1, 2, 0, 1, 2, 1, 2, 0, 0, 0, 1]
low=0
mid=0
high=len(arr)-1
while mid<=high:
    if arr[mid]==0:
        arr[mid],arr[low]=arr[low],arr[mid]
        mid+=1
        low+=1
    elif arr[mid]==1:
        mid+=1
    else:
        arr[mid],arr[high]=arr[high],arr[mid]
        high-=1
print(arr)
    
    
