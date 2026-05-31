arr=[1,2,3,4,5,6,7]
i=arr[0]
for j in range (1,len(arr)):
    arr[j-1]=arr[j]
arr[len(arr)-1]=i
print(arr)
