n=input("enter num: ")
ln=len(n)
s=0
for i in n:
    s+=int(i)**ln
if int(n)==s:
    print("Armstrong")
else:
    print("Not armstrong")
