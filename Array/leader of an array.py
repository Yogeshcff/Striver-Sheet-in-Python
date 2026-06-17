# #Brute force

# arr=[10,22,12,3,0,6]
# ans=[]
# for i in range (len(arr)):
#     leader=True
#     for j in range (i,len(arr)):
#         if arr[j]>arr[i]:
#             leader=False
#             break
#     if leader == True:
#         ans.append(arr[i])
# print(ans)
     

# optimal solution

ans=[]
arr=[10,22,12,3,0,6]
maxi=float('-inf')
for i in range (len(arr)-1,-1,-1):
    
    if arr[i]>maxi:
        maxi=arr[i]
        ans.append(maxi)
ans.reverse()
print(ans)