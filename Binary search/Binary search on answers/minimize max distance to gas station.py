# #brute force


# arr=[1,13,17,23]
# placed=[0]*(len(arr)-1)
# k=5
# for gas in range (1,k+1):
#     max_val=-1
#     max_index=-1
#     for i in range (0,len(arr)-1):
#         diff=arr[i+1]-arr[i]
#         section_lenght=diff/(placed[i]+1)
#         if max_val<section_lenght:
#             max_val=section_lenght
#             max_index=i
#     placed[max_index]+=1
# # print(placed)
# ans=-1
# for i in range (0,len(arr)-1):
#     diff=arr[i+1]-arr[i]
#     section_lenght=diff/(placed[i]+1)
#     ans=max(ans,section_lenght)
# print(ans)
    
    
#better solution
# import heapq
# arr=[1,13,17,23]

# k=5
# n=len(arr)
# heap=[]
# placed=[0]*(n-1)
# for i in range (n-1):
#     diff=arr[i+1]-arr[i]
#     heapq.heappush(heap,(-diff,i))
# for i in range (k):
#     max_lenght , index=heapq.heappop(heap)
#     placed[index]+=1
#     new_lenght=(arr[index+1]-arr[index])/(placed[index]+1)
#     heapq.heappush(heap,(-new_lenght,index))
# ans=heapq.heappop(heap)
# print(-ans[0])
    
#optimal solution using binary search
def check(arr, dist, k):
    count = 0
    for i in range(len(arr)-1):
        gap = arr[i+1] - arr[i]
        count += int(gap/dist)
        if gap % dist == 0:
            count -= 1
    return count <= k 
arr=[1,13,17,23]
k=5
low=0
high=max(arr[i+1]-arr[i] for i in range (len(arr)-1))
while high-low>1e-6:
    mid=low+(high-low)/2.0
    if check(arr,mid,k):
        high=mid
    else:
        low=mid
print(high)
    