arr=[3,2,1]
index=-1
n=len(arr)
for i in range (n-2,-1,-1):
    if arr[i+1]>arr[i]:
        index=i
        print(index)
        break
if index==-1:
    arr[:]=arr[:][::-1]
    print(arr)
else:
    for i in range (n-1,index,-1):
        if arr[i]>arr[index]:
            arr[i],arr[index]=arr[index],arr[i]
            break
    arr[index+1:]=arr[index+1:][::-1]
    print(arr)