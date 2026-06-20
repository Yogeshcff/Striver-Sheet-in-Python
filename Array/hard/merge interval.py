intervals = [[1,4],[4,5]]
start=intervals[0][0]
merge=[]

n=len(intervals)
c=2
for i in range (n-1):
    if intervals[i][c-1]>=intervals[i+1][0]:
        end=intervals[i+1][c-1]
        new=[start,end]
        if new not in merge:
            merge.append(new)
    
    else:
        start=intervals[i+1][0]
        merge.append(intervals[i+1])
print(merge)        
        
    
        