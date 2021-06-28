f=open('Table.txt','r')
n=int(input('Enter the number of lime: '))
for i in range(n):
       p=f.readline()
       print(p)
f.close()