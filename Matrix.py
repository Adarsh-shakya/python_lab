#print matrix
r=int(input("enter the row: "))
c=int(input("enter the column: "))
matrix=[]
for i in  range(r):
    a=[]
    for j in range(c):
        k=int(input("Enter the element of the matrix: "))
        a.append(k) 
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()    
