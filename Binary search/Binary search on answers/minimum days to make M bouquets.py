bloomDay=[1,10,3,10,2]
m=3
k = 1
def check(bloomDay,m,k,day):
    bloom=0
    bouquet=0
    for i in bloomDay:
        if day>=i:
            bloom+=1
            if bloom==k:
                bouquet+=1
                bloom=0
        else:
            bloom=0
    return bouquet

            

high=max(bloomDay)
low=min(bloomDay)
ans=high
if m*k>len(bloomDay):
    print(-1)
    exit()
while low<=high:
    mid=low+(high-low)//2
    if check(bloomDay,m,k,mid)>=m:
        ans=min(ans,mid)
        high=mid-1
    else:
        low=mid+1
print(ans)
    
    
    
    
#brute force solution
# ans=max(bloomDay)
# for i in bloomDay:
#     if check(bloomDay,m,k,i)>=m:
#         ans=min(ans,i)
# print(ans)