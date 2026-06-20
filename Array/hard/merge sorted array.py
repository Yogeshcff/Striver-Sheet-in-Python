#Brute force

# ans=[]
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# i=0
# j=0
# while i<m and j <n:
#     if nums1[i]<nums2[j]:
#         ans.append(nums1[i])
#         i+=1
#     else:
#         ans.append(nums2[j])   
#         j+=1
# while j<m:
#     ans.append(nums2[j])
#     j+=1
# while i<n:
#     ans.append(nums1[i])
#     i+=1
# print(ans)
# for i in range (m+n):
#     nums1[i]=ans[i]
# print(nums1)


#optimal approach
nums1 = [0]
m = 0
nums2 = [1]
n = 1
i=m-1
j=n-1
k=m+n-1
while i>=0 and j>=0:
    if nums1[i]>nums2[j]:
        nums1[k]=nums1[i]
        i-=1
    else:
        nums1[k]=nums2[j] 
        j-=1
    k-=1

while j>=0:
    nums1[k]=nums2[j]
    j-=1
    k-=1
print(nums1)