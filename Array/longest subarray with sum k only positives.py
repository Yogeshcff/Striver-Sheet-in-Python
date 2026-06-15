#Brute force

# arr=[1,2,3,1,1,1,1,4,2,3]

# kk=3
# longest=0
# for i in range (len(arr)):
    
#     for j in range (i,len(arr)):
#         sum=0
#         for k in range (i,j+1):
#             sum+=arr[k]
#         if sum==kk:
#             longest=max(longest,j-i+1)
# print(longest)

#slightly better

# arr=[1,2,3,1,1,1,1,4,2,3]
# kk=3
# lenght=0
# for i in range (len(arr)):
#     s=0
#     for j in range (i,len(arr)):
#         s+=arr[j]
#         if s==kk:
#             lenght=max(lenght,j-i+1)
# print(lenght)

#optimal approach for positives and zeroes only

# arr=[3,-1,1]
# j=0
# i=0
# maxx=0
# sum=0
# k=2
# while j<len(arr):
#     if sum>k:
#         sum=sum-arr[i]
#         i=i+1
#     elif sum<k:
#         sum+=arr[j]
#         j+=1
#     else:
#         maxx=max(maxx,j-i)
#         sum-=arr[i]
#         i+=1
# print(maxx)
# arr=[1,1]
# left=0
# right=0
# maxlen=0
# sum=arr[0]
# k=2
# n=len(arr)
# while right<n:
#     while left<=right and sum>k:
#         sum-=arr[left]
#         left+=1
#     if sum==k:
#         maxlen=max(maxlen,right-left+1)
#     right+=1
#     if right<n:
#         sum+=arr[right]
# print(maxlen)


#optimal approach for array with negatives

arr=[3,-1,1]
prefixsum=0
prefixmap={}
k=2
maxlen=0

for i , num in enumerate(arr):
    prefixsum+=num

    if prefixsum==k:
        maxlen=max(maxlen,i+1)

    target=prefixsum-k
    if target in prefixmap:
        lenght=i-prefixmap[target]
        maxlen=max(maxlen,lenght)

    if prefixsum not in prefixmap:
        prefixmap[prefixsum]=i
print(maxlen)