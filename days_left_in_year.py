#enter the date as dd mm yyyy and find the days are left
dd, mm, yy =input("Enter the date with space seprated: ").split()
m=int(mm)
i=int(dd)
if m==1:
    d=365-i
    print("Days are left",d)
elif m==2:
    d=365-(31+i)
    print("Days are left",d)
elif m==3:
    d=365-(31+28+i)
    print("Days are left",d)
elif m==4:
    d=365-(31*2+28+i)
    print("Days are left",d)
elif m==5:
    d=365-(31*2+28+30+i)
    print("Days are left",d)
elif m==6:
    d=365-(31*3+28+30+i)
    print("Days are left",d)
elif m==7:
    d=365-(31*3+28+30*2+i)
    print("Days are left",d)
elif m==8:
    d=365-(31*4+28+30*2+i)
    print("Days are left",d)
elif m==9:
    d=365-(31*5+28+30*2+i)
    print("Days are left",d)
elif m==10:
    d=365-(31*5+28+30*3+i)
    print("Days are left",d)
elif m==11:
    d=365-(31*6+28+30*3+i)
    print("Days are left",d)
elif m==12:
    d=365-(31*6+28+30*4+i)
    print("Days are left",d)    
