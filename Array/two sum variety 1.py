arr=[5,2,8,6,11]
left=0
n=len(arr)
sum=14
right=n-1
arr.sort()

found=False
while left<=right:
    if arr[left]+arr[right] ==sum:
        print("Yes")
        found=True
        break
    elif arr[left]+arr[right] < sum:
        left+=1
    else:
        right=right-1
if found==False:
    print("No")
    