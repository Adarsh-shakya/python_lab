# Find the factorial of given number
n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
else:
    print("factorial of given num is: ",fact)
