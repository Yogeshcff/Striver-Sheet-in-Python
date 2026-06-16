# #brute force

# arr=[3,1,-2,-5,2,-4]
# n=len(arr)
# pos_list=[]
# neg_list=[]
# for i in arr:
#     if i>=0:
#         pos_list.append(i)
#     else:
#         neg_list.append(i)
# print(pos_list,neg_list)
# for i in range (n//2):
#     arr[2*i]=pos_list[i]
#     arr[2*i+1]=neg_list[i]
# print(arr)

#optimal solution only one pass
arr=[3,1,-2,-5,2,-4]
n=len(arr)
pos_index=0
neg_index=1
ans=[0]*n
for i in arr:
    if i >0:
        ans[pos_index]=i
        pos_index+=2
    else:
        ans[neg_index]=i
        neg_index+=2
print(ans)
        
#variety 2 where number of positives and negatives are not equal
arr=[-1,2,3,4,-3,1,-9,-7,-5]
pos=[]
neg=[]
n=len(arr)
for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
mini=min(len(pos),len(neg))
maxi=max(len(pos),len(neg))

for j in range (mini):
    arr[j*2]=pos[j]
    arr[j*2+1]=neg[j]
if len(pos)>len(neg):
    index=mini*2
    for k in range (mini,maxi):
        arr[index]=pos[k]
        index+=1
else:
    index=mini*2
    for k in range (mini,maxi):
        arr[index]=neg[k]
        index+=1
    
print(arr)