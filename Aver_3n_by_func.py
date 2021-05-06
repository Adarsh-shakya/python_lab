#Average of three number by function:
def sum(a,b,c):
    s=a+b+c
    return s
def aver(x,y,z):
    sm=sum(x,y,z)
    return sm/3
num1=int(input('Enter the number: '))
num2=int(input('Enter the number: '))
num3=int(input('Enter the number: '))
print('Average of three number: ',aver(num1,num2,num3))
