#brute force using linear search to find square root


# ans=0
# n=30
# for i in range (1,n):
#     if i*i<=n:
#         ans=i
#     else:
#         break
# print(ans)


#using binary search
n=100
low=1
high=n
ans=0
while low<=high:
    mid=low+(high-low)//2
    if mid*mid==n:
        ans=mid
        break
    elif mid*mid>n:
        high=mid-1
    else:
        ans=mid
        low=mid+1
print(ans)
        
    