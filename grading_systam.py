#School grading systam:
m=int(input("Enter the marks : "))
if m<25:
    print("Grad F")
elif 25<=m<45:
    print("Grad E")
elif 45<=m<50:
    print('Grad D')
elif 50<=m<60:
    print('Grad C')
elif 60<=m<80:
    print('Grad B')
elif m<=80:
    print('Grad A')
