# #brute force

# arr=[1,1,1]
# k=2
# count=0

# for i in range (len(arr)):
#     sum=0
#     for j in range (i,len(arr)):
#         sum+=arr[j]
#         if sum==k:
#             count+=1
# print(count)

# #Optimal solution using prefix sum

arr=[1,2,3,-3,1,1,1,4,2,-3]
prefix_map={0:1}
prefix_sum=0
count=0
k=3
for i in range (len(arr)):
    prefix_sum+=arr[i]
    target=prefix_sum-k
    count+=prefix_map.get(target,0)
    prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
print(count)
