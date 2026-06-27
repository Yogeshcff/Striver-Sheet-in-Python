a = 3
timeperunit = 1
board = [10,20,30,40]
def check(board,maxtime,painter,timeperunit):
    painter=1
    curboard=0
    for i in board:
        if i*timeperunit>maxtime:
            return False
        if i*timeperunit + curboard>maxtime:
            painter+=1
            curboard=i*timeperunit
        else:
            curboard+=i*timeperunit
    return painter<=a
low=max(board)*timeperunit
high=timeperunit*sum(board)
while high>=low:
    mid=low+(high-low)//2
    if check(board,mid,a,timeperunit):
        high=mid-1
    else:
        low=mid+1
print(low)
    