# #Brute force
# arr=[1,1,2,3,3,4,4]

# for i in range (len(arr)):
#     count=0
#     for j in range (len(arr)):
#         if arr[i]==arr[j]:
#             count+=1
#     if count==1:
#         print(arr[i])

# Better solution using hashmap


#find maximum element
# arr=[1,1,2,3,3,4,4]
# maxx=arr[0]
# for i in range (len(arr)):
#     maxx=max(maxx,arr[i])

# hash=[0]*(maxx+1)
# for j in range (0,len(arr)):
#     hash[arr[j]]+=1
# for k in range (len(arr)):
#     if hash[arr[k]]==1:
#         print(arr[k])


#Optimal solution
arr=[1,1,2,3,3,4,4]
xor=0
for i in range (len(arr)):
    xor=xor^arr[i]
print(xor)