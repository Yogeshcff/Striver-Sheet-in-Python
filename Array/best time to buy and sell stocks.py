arr=[7,1,5,3,6,4]
minn=arr[0]
profit=0
for i in range (1,len(arr)):
    cost=arr[i]-minn
    profit=max(profit,cost)
    minn=min(minn,arr[i])
print(profit)