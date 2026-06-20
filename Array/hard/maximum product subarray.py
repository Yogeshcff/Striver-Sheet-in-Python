# arr=[1,2,-3,0,-4,-5]
# ans=float('-inf')
# n=len(arr)
# pre=1
# suf=1
# for i in range(n):
    
#     if pre==0:
#         pre=1
#     if suf==0:
#         suf=1
            
#     pre=pre*arr[i]
#     suf=suf*arr[n-i-1]
#     ans=max(pre,ans,suf)
# print(ans)


#brute force

# arr=[1,2,-3,0,-4,-5]
# ans=float('-inf')
# for i in range (len(arr)):
#     pro=arr[i]
#     for j in range (i+1,len(arr)):
#         pro*=arr[j]
#         ans=max(ans,pro)
# print(ans)
        