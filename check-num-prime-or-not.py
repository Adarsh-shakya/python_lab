# find number is prime or not
a=int(input("Enter the number: "))
i=2
while i<a:
    if a%i==0:
        break
    i=i+1
else:
    print("number is prime")
if i!=a:
    print("number is not prime")
