num=7
arr=[1,2,3,4,5,6,7,8,9]
for i in  range (len(arr)):
    if arr[i]==num:
        print(i)
    elif num  not in arr:
        print(-1)