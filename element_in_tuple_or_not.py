#check whether an element exists within a tuple.
n=int(input("Enter any  number: "))
t=(3,4,7,6,0,10,5,11,97,34)
for i in t:
    if n==i:
        print('Entered element is exist in the tuple')
        break
else:
    print('Entered element is not exist in the tuple')
