r=int(input('Enter the row of matrix: '))
c=int(input('Enter the column of matrix: '))
matrixA=[]
for i in range(r):
    a=[]
    for j in  range(c):
        k=int(input("Enter the element of matrix A: "))
        a.append(k)
    matrixA.append(a)    
matrixB=[]
for i in range(r):
    a=[]
    for j in  range(c):
        k=int(input("Enter the element of matrix B : "))
        a.append(k)
    matrixB.append(a)
matrixC=[]    
for i in range(r):
    a=[]
    for j in range(c):
        a.append(matrixA[i][j]+matrixB[i][j])
    matrixC.append(a)
for i in range(r):
    for j in range(c):
        print(matrixC[i][j],end=' ')
    print()    
