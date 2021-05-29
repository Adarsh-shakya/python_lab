#create dict with square of keys
dct={}
n=int(input('Enter the number: '))
for i in range(n):
    dct[i+1]=(i+1)**2
print(dct)    
