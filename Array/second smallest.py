arr=[1,2,3,4,5,6,7,8,9]
smallest=arr[0]
ss=float('inf')
for i in range (len(arr)):
    if arr[i]<smallest:
        ss=smallest
        smallest=arr[i]
    elif arr[i]!=smallest and arr[i]<ss:
        ss=arr[i]
print(ss)