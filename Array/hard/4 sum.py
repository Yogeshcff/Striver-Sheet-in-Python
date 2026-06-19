# #brute force 

# nums=[1,0,-1,0,-2,2]
# n=len(nums)
# target=0
# ans=[]
# for i in range (n):
#     for j in range (i+1,n):
#         for k in range (j+1,n):
#             for l in range (k+1,n):
#                 sum=nums[i]+nums[j]+nums[k]+nums[l]
#                 if sum==target:
#                     tri=sorted([nums[i],nums[j],nums[k],nums[l]])
#                     if tri not in ans:
#                         ans.append(tri)
# print(ans)

#better solution using hashmap
# nums=[]
# n=len(nums)
# target=0
# ans=[]
# for i in range (n):
#     for j in range (i+1,n):
#         map={}
#         for k in range (j+1,n):
#             sum=target-(nums[i]+nums[j]+nums[k])
#             if sum in map:
#                 tri=sorted([nums[i],nums[j],nums[k],sum])
#                 if tri not in ans:
#                     ans.append(tri)
#             map[nums[k]]=k
# print(ans)


#optimal approach

nums=[1,1,1,2,2,2,3,3,3,4,4,4,5,5]
n=len(nums)
nums.sort()
ans=[]
target=8
for i in range (n):
    if i > 0 and nums[i]==nums[i-1]:
        continue
    for j in range (i+1,n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        k=j+1
        l=n-1
        while k<l:
            sum=nums[i]+nums[j]+nums[k]+nums[l]
            if sum < target:
                k+=1
            elif sum > target:
                l-=1
            else:
                
                tri=[nums[i],nums[j],nums[k],nums[l]]
                if tri not in ans:
                    ans.append(tri)
                while k<l and nums[k]==nums[k+1]:
                    k+=1
                while k<l and nums[l]==nums[l-1]:
                    l-=1
                k+=1
                l-=1
print(ans)
                                
