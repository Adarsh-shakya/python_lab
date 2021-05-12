#Remove the item from the set
a=set()
for i in range(6):
    k=int(input('Enter the number : '))
    a.add(k)
print(a)    
n=int(input('Enter the number which you want to remove: '))
a.discard(n)
print(a)
