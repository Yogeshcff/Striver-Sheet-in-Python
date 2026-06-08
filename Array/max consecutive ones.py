nums=[1,1,1,0,0,1,0,1,0,0,1,1,1,1,0,1]
count=0

max_count=0
for i in range (0,len(nums)):
    if nums[i]==1:
        count+=1
    else:
        count=0
    if max_count<count:
        max_count=count
print(max_count)