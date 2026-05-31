def leftrotateb_by_k(k):
    
    arr=[1,2,3,4,5,6,7]
    k=k%len(arr)
    temp=arr[0:k]
    for i in range (k,len(arr)):
        arr[i-k]=arr[i]
    for j in range (len(arr)-k,len(arr)):
        arr[j]=temp[j+k-len(arr)]
    return arr
print(leftrotateb_by_k(7))

