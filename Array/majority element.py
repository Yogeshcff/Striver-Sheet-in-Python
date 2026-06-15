# # brute force 
# arr=[2,2,3,3,1,2,2]
# n=len(arr)
# for i in range (n):
#     count=0
#     for j in range(0,n):
#         if arr[i]==arr[j]:
#             count+=1
#     if count>n/2:
#         print(arr[i])
#     else:
#         print(-1)

#better solution
# arr=[2,2,3,3,1,2,2]
# hashmap={}

# for i , num in enumerate(arr):
#     hashmap[num]=hashmap.get(num,0)+1
# print(hashmap)
# for j in hashmap:
#     if hashmap[j]>len(arr)/2:
#         print(j)

#Optimal solution using moore's voting algorithm

arr=[2,2,3,3,1,2,2]
count=0
element=0
for i in range (len(arr)):
    if count==0:
        element=arr[i]
        count+=1
    elif arr[i]==element:
        count+=1
    else:
        count-=1
print(element)