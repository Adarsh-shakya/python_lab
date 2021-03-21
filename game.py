import random
a=int(input("enter number 1 to 3: "))
n=random.randint(1,3)
if a==n:
    print("you win")
    print("because computer is also chooe ",n)
else:
    print("you loss")
    print("because computer choose ",n)
