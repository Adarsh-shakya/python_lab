# print matrix
n=int(input('Enter the number of row: '))
m=[]
for i in range(n):
    k=list(map(int, input('Enter the row of matrix: ').split()))
    m.append(k)
for j in m:
    print(*j)
