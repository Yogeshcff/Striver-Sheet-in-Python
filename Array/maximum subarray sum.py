# #brute force
# arr=[-2,-3,-4,-1,-2,-1,-5,-3]
# maxx=float('-inf')
# for i in range (len(arr)):
#     sum=0
#     for j in range (i,len(arr)):
#         sum+=arr[j]
#         maxx=max(maxx,sum)
# print(maxx)

#optimal solution kodane's algorithm

arr=[-2,-3,4,-1,-2,1,5,-3]
sum=0
maxx=float('-inf')
for i in range (len(arr)):
    sum+=arr[i]
    maxx=max(maxx,sum)
    if sum<0:
        sum=0
print(maxx)

#printing the maximum subarray
# arr=[-2,-3,4,-1,-2,1,5,-3]
# sum=0
# ans_start=-1
# ans_end=-1
# maxx=float('-inf')
# for i in range (len(arr)):
    
#     if sum<=0:
#         sum=0
#         start=i
    
#     sum+=arr[i]
#     if sum>maxx:
#         maxx=sum
#         ans_start=start
#         ans_end=i
    
# print(arr[ans_start:ans_end+1])