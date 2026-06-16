arr=[2,1,5,3,4,0,0]
index=-1
n=len(arr)
for i in range (n-2,-1,-1):
    if arr[i]<arr[i+1]:
        index=i
        break
if index==-1:
    print(arr[::-1])
else:
    for i in range (n-1,index,-1):
        if arr[i]>arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            break
    arr[index+1:]=arr[index+1:][::-1]
print(arr)