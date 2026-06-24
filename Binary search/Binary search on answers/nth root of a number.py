#brute force


# def multi(num,n):
#     ans=1
#     for i in range (n):
#         ans*=num
#     return ans
# n=int(input("enter the nth root : "))
# m=int(input('enter the number : '))
# ans=-1
# for i in range (1,m+1):
#     if multi(i,n)==m:
#         ans=i
#         break
# print(ans)
    
    


#using binary search
def multi(num,n):
    ans=1
    for i in range (n):
        ans*=num
    return ans
n=3
m=64
ans=-1
low=1
high=m
while low<=high:
    mid=low+(high-low)//2
    if mid**n==m:
        ans=mid
        break
    elif mid**n<m:
        low=mid+1
    else:
        high=mid-1
print(ans)
        
        