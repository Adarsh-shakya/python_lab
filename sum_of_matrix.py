#sum of two matrix 
l=int(input('Enter the number of row: '))
m=[]
n=[]
o=[]
for x in range(2):
    print('Enter the element for matrix')
    for i in range(l):
        k=list(map(int, input('Enter the row of matrix: ').split()))
        if x==0:
          m.append(k)
        else:
          n.append(k)
for j in range(l):
    s=[]
    for i in range(len(m[0])):
        s.append(m[j][i]+n[j][i])
    o.append(s)
for h in o:
    print(*h)
