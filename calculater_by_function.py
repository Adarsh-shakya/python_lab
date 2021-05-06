#caculater by the function
def calculater(x,y):
    return x+y,x-y,x*y,x/y,x%y
a=int(input('Enter the number:'))
b=int(input('Enter the number: '))
add,sub,mult,div,mod=calculater(a,b)
print('Sum of two number        : ',add)
print('subtraction of two number: ',sub)
print('product of two nnumber   : ',mult)
print('Divisionof two number    : ' ,div)
print('Modulo of two number     : ',mod)
