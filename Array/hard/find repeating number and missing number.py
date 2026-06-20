#brute force

# arr=[4,3,6,2,1,1]
# arr.sort()
# for i in range (len(arr)):
#     if arr[i]^arr[i+1]==0:
#         print(arr[i])
#         break
# for i in range (len(arr)):
#     if arr[i+1]-arr[i]==2:
#         print(arr[i]+1)
#         break

# arr=[4,3,6,2,1,1]
# for i in range (1,len(arr)+1):
#     count=0
#     for j in range (0,len(arr)):
#         if arr[j]==i:
#             count+=1
#     if count==2:
#         print(i)
#     elif count==0:
#         print(i)


# using hashing
# arr=[4,3,6,2,1,1]
# map=[0]*(len(arr)+1)
# for i in range (len(arr)):
#     map[arr[i]]+=1
# print(map)
# for i in range (1,len(map)):
#     if map[i]==2:
#         print(i)
#     if map[i]==0:
#         print(i)

#using maths

arr=[4,3,6,2,1,1]
n=len(arr)
sn=(n*(n+1))/2
s2n=(n*(n+1)*(2*n+1))/6
s=0
s2=0
for i in range (n):
    s+=arr[i]
    s2+=arr[i]*arr[i]
var1=s-sn
var2=s2-s2n
var2=var2/var1
rep=(var1+var2)/2
mis=rep-var1
print(rep,mis)

