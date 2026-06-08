# # Brute force

# arr1=[1,1,2,3,4,4,5,5]
# arr2=[2,3,4,5,6,7]
# sett=set()
# for i in range (len(arr1)):
#     sett.add(arr1[i])
# for j in range (len(arr2)):
#     sett.add(arr2[j])
# print(list(sett))


# Optimal solution

arr1=[1,1,2,3,4,5]
arr2=[2,3,4,4,5,6]
n1=len(arr1)
n2=len(arr2)
i=0
j=0
l=[]
while (i<n1 and j<n2):
    if arr1[i]<=arr2[j]:
        if len(l)==0 or l[-1]!=arr1[i]  : 
            l.append(arr1[i])
        i+=1
    else:
        if len(l)==0 or l[-1]!=arr2[j]  :
            l.append(arr2[j])
        j+=1
while i<n1:
    if len(l)==0 or l[-1]!=arr1[i]:
        l.append(arr1[i])
    i+=1
while j<n2:
    if len(l)==0 or l[-1]!=arr2[j]:
        l.append(arr2[j])
    j+=1
print(l)

    
