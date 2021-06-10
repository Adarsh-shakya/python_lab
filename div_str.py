#divide a string in some parts
st=input('Enter the string: ')
n=int(input('Enter the number of parts: '))
lst=['']*n
count=len(st)//n
j=0
for p in range(n):
    lst[p]=st[j:j+count]
    j+=count
print(lst)    
