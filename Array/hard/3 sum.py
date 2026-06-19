# #brute force

# arr=[-1,0,1,2,-1,-4]
# ans=[]

# n=len(arr)
# for i in range (len(arr)):
#     for j in range (i+1,n):
#         for k in range (j+1,n):
            
#             if arr[i]+arr[j]+arr[k]==0:
#                 tri=sorted([arr[i],arr[j],arr[k]])
#                 if tri not in ans:
#                     ans.append(tri)
                    
# print(ans)

#better solution

# arr=[-1,0,1,2,-1,-4]
# ans=[]
# for i in range (len(arr)):
#     map={}
#     for j in range (i+1,len(arr)):
#         k=-(arr[i]+arr[j])
#         if -(arr[i]+arr[j]) in map:
#             tri=sorted([arr[i],arr[j],k])
#             if tri not in ans:
#                 ans.append(tri)
#         map[arr[j]]=j
# print(ans)
        
        
#optimal solution

nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
nums.sort()
ans=[]
for i in range (len(nums)):
    if i>0 and nums[i]== nums[i-1] :
        continue
    j=i+1
    k=len(nums)-1
    while j<k:
        sum=nums[i]+nums[j]+nums[k]
        if sum<0:
            j+=1
        elif sum>0:
            k-=1
        else:
            ans.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
            while j< k and nums[j]==nums[j-1]:
                j+=1
            while j<k and nums[k]==nums[k+1]:
                k-=1
print(ans)
                    