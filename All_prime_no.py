# find all prime number in given intervl
ni, nf = input('Enter the interval: ').split()
n1=int(ni)
n2=int(nf)
print('list of prime number:')
for i in range(n1,n2+1):
    for x in range(2,i):
        if i%x==0:
            break
    else:
        print(i)
