# Brute force solution

# arr1=[1,2,2,3,3,4,5,6]
# arr2=[2,3,3,5,6,6,7]
# a=len(arr1)
# b=len(arr2)
# vis=[0]*b
# ans=[]
# for i in range (0,a):
#     for j in range (0,b):
#         if arr1[i]==arr2[j] and vis[j]==0:
#             ans.append(arr1[i])
#             vis[j]=1
#             break
#         elif arr2[j]>arr1[i]:
#             break
# print(ans)

# Optimal solution

arr1=[1,2,2,3,3,3,4,5,6]
arr2=[2,3,3,3,5,6,6,7,7,7,7,7]
a=len(arr1)
b=len(arr2)
j=0
i=0
ans=[]
while i<a and j<b:
    if arr1[i]<arr2[j]:
        i+=1    
    elif arr1[i]>arr2[j]:
        j+=1
    else:
        ans.append(arr1[i])
        j+=1
        i+=1
print(ans)

