#brute force

# k=6
# arr=[4,2,2,6,4]
# count=0
# for i in range (len(arr)):
#     xor=0
#     for j in range (i,len(arr)):
#         xor=xor^arr[j]
#         if xor==k:
#             count+=1
# print(count)


#optimal solution using hashmap
k=2
arr=[1,2,3,2]
count=0
map={0:1}
xor=0
for i in range (len(arr)):
    xor=xor^arr[i]
    x=xor^k
    if x in map:
        count+=map.get(x,0)
    map[xor]=map.get(xor,0)+1
print(count)
    