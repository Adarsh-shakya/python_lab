f=open('Table.txt','w')
for i in range(1,11):
    for j in range(1,11):
        f.write(str(i*j)+'\t')
        print(i*j ,end='\t')
    f.write('\n')
    print()
f.close()
