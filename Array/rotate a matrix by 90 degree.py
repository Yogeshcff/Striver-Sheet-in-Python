# #brute force

# matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# r=len(matrix)
# c=len(matrix[0])
# new_matrix=[[0]*r for _ in range (r)]
# print(new_matrix)
# for i in range (r):
    
#     for j in range (c):
#         k=3-j
#         # new_matrix[i][j]=matrix[k][i]
#         new_matrix[j][r-i-1]=matrix[i][j]
        
# print(new_matrix)
# matrix=new_matrix
# print(matrix)

#optimal solution in place

matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(matrix)
for i in range(n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
print(matrix)
for i in matrix:
    i.reverse()
print(matrix)