n=int(input("Enter the salary: "))
n1=int(input("Enter the year of service: "))
if n1>5:
    bonus=(n/100)*5
    total_salary=n+bonus
    print("total salary=", total_salary)
else:
    print("total salary=", n)
