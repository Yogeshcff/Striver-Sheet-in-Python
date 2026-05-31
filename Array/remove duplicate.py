arr=[1,1,2,3,4,5,5,6,6,6,6,7]
i=0
for j in range (len(arr)):
    if arr[j]!=arr[i]:
        arr[i+1]=arr[j]
        i+=1
print(i+1)