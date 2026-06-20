 #variety one given row and column print the element
 
# def ncr(n,r):
#     res=1
#     for i in range (r):
#         res=res*(n-i)
#         res=res/(i+1)
#     return res
# row=5
# col=3
# a=ncr(row-1,col-1)
# print(a)


#variety 2 print entire row

# row=5
# for i in range (1,row+1):
    # print(ncr(row-1,i-1))


# n=5    
# ans=1
# print(ans)
# for i in range (1,n):
#     ans=ans*(n-i)
#     ans=ans/i
#     print(ans)
#optimal solution to print entire pascal's triangle

numRows=5
def roww(numRows):
    ans=1
    l=[1]
    for i in range (1,numRows):
        ans=ans*(numRows-i)
        ans=ans/i
        l.append(int(ans))
    return l
x=[]
for j in range (1,numRows+1):
    a=roww(j)
    x.append(a)
print(x)