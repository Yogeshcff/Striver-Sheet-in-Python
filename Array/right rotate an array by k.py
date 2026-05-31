arr=[1,2,3,4,5,6,7,8]
k=3
arr[:]=arr[:][::-1]
arr[0:k]=arr[0:k][::-1]
arr[k:]=arr[k:][::-1]
print(arr)