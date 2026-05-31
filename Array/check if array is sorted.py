def checksorted():
    arr=[1,0,3,4,5]
    for i in range (1,len(arr)):
        if arr[i]>arr[i-1]:
            continue
        else:
            return False
    return True
print(checksorted())
print("completed")