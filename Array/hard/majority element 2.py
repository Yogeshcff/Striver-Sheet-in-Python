# better solution

# arr=[2,2]
# hashmap={}
# min=len(arr)//3 +1
# ans=[]
# for i in arr:
#     hashmap[i]=hashmap.get(i,0)+1
#     if hashmap[i]==min:
#         ans.append(i)
# print(ans)


# optimal soluution moore voting algorithm
nums=[2,1,1,3,1,4,5,6]
c1=0
c2=0
e1=0
e2=0
for i in range (len(nums)):
    if c1==0 and nums[i]!=e2:
        c1=1
        e1=nums[i]
    elif c2==0 and nums[i]!=e1:
        c2=1
        e2=nums[i]
    elif nums[i]==e1:
        c1+=1
    elif nums[i]==e2:
        c2+=1
    else:
        c1-=1
        c2-=1
ans=[]
c1=0
c2=0
for i in nums:
    if i==e1:
        c1+=1
    if i==e2:
        c2+=1
mini=len(nums)//3 + 1
if c1>=mini:
    ans.append(e1)
if c2>=mini and e1!=e2:
    ans.append(e2)
print(ans)
    
    