#sum of two matrix 
l=int(input('Enter the number of row for matrix: '))
m=[]
n=[]
o=[]
for x in ['A','B']:
    print('Enter the element for matrix',x)
    for i in range(l):
        k=list(map(int, input(f'Enter the {i} row of matrix: ').split()))
        m.append(k) if x=='A' else n.append(k)
for j in range(l):
    s=[]
    for i in range(len(m[0])):
        s.append(m[j][i]+n[j][i])
    o.append(s)
for h in o:
    print(*h)
