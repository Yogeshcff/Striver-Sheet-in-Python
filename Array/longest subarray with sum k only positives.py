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

#optimal approach

arr=[1,2,3,1,-1,1,0,1,1,1,3,3]
j=0
i=0
maxx=0
sum=0
k=7
while j<len(arr):
    if sum>k:
        sum=sum-arr[i]
        i=i+1
    elif sum<k:
        sum+=arr[j]
        j+=1
    else:
        maxx=max(maxx,j-i)
        sum-=arr[i]
        i+=1
print(maxx)