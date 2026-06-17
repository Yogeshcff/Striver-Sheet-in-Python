# # #Brute force

# # arr=[102,4,100,1,101,3,2,1,1,5]
# # longest=1
# # for i in range (len(arr)):
# #     count=1
# #     x=arr[i]
# #     while x+1 in arr:
# #         count+=1
# #         x+=1
# #     if count>longest:
# #         longest=count
# # print(longest)

# #Better solution

# arr=[100,102,100,101,101,4,3,2,3,2,1,1,1,2]
# arr.sort()
# count=1
# longest=0
# lastsmallest=float('-inf')
# for i in range (len(arr)):
#     if arr[i]-1==lastsmallest:
#         count+=1
#         lastsmallest=arr[i]
#     elif arr[i]==lastsmallest:
#         continue
#     else:
#         count=1
#         lastsmallest=arr[i]
#     longest=max(longest,count)
# print(longest)


#optimal solution

arr=[102,4,100,1,101,3,2,1,1]
n=len(arr)
sett=set(arr)
longest=1
if n==0:
    print(0)
for i in sett:
    if i-1 not in sett:
        count=1
        current=i
        while current+1 in sett:
            count+=1
            current+=1
        longest=max(longest,count)
print(longest)        
    
