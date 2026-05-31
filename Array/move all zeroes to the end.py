arr=[1,2,0,2,3,0,0,3,4,0,5,0,7,0,0,9]
j=-1
for k in range (len(arr)):
    if arr[k]==0:
        j=k
        break
for i in range (j,len(arr)):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j=j+1
print(arr)