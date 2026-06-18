# #Brute force

# matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
# def markinfinty(matrix,row,col):
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range  (r):
#         if matrix[i][col]!=0:
#             matrix[i][col]=float('inf')
            
#     for j in range (c):
#         if matrix[row][j]!=0:
#             matrix[row][j]=float('inf')
# r=len(matrix)
# c=len(matrix[0])
# for i in range (r):
#     for j in range (c):
#         if matrix[i][j]==0:
#             markinfinty(matrix,i,j)
# for i in range (r):
#     for j in range (c):
#         if matrix[i][j]==float('inf'):
#             matrix[i][j]=0
# print(matrix)
        
        
#optimal solution
matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
r=len(matrix)
c=len(matrix[0])
row_track=[0]*r
column_track=[0]*c
for i in range (r):
    for j in range (c):
        if matrix[i][j]==0:
            row_track[i]=-1
            column_track[j]=-1
for i in range (r):
    for j in range (c):
        if row_track[i]==-1 or column_track[j]==-1:
            matrix[i][j]=0

print(matrix)