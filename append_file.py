f=open('sum.txt','a')
n1=eval(input('Enter the first number: '))
n2=eval(input('Enter the secand number: '))
sum=n1+n2
r=f'sum of {n1} and {n2} is {sum}\n'
f.write(r)
print(r)
f.close()