arr= [1,2,3,2,5,3,7,1,0,2]
largest = arr[0]
for i in range (0 , len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print(largest)