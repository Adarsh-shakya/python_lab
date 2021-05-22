n=int(input('Enter the amount: '))
x=n-100
p=int(x/2000)
s=x-(p*2000)
h=int(s/500)
r=s-(h*500)
d=int((r/100)+1)
print'notes of 2000:',p
print'notes of 500:',h
print'notes of 100:',d
