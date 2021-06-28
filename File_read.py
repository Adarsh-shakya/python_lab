f=open("sum.txt",'r')
count=0
for i in f:
    count+=1
    print(i,end='')
print('number of line is ',count)