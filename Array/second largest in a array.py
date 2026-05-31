arr=[1,2,3,4,6,79,5,9]
largest=arr[0]
sl=-1
for i in range (len(arr)):
    if arr[i]>largest:
        sl=largest
        largest=arr[i]
    elif arr[i]<largest and arr[i]>sl:
        sl=arr[i]
print(sl)
