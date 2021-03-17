''' Perfect number n=6 factor of 6 are 1,2,3
    1x2x3=1+2+3
        6=6    and n=28          '''
n=int(input("Enter the number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("Given number is perfect")
else:
    print("Given number is not perfect")
