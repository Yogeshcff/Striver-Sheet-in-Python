arr=[1,2,3,4,5,7,8,9,10]
n=len(arr)+1
sum=0
ts=(n*(n+1))/2
for i in range (len(arr)):
    sum+=arr[i]
print(ts-sum)