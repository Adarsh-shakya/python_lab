n=int(input('Enter the quantity: '))
t_cost=n*100
if t_cost>=1000:
    descount=(t_cost/100)*10
    cost=t_cost-descount
    print("Total_cost=",cost)
else:
    print("Total_cost=",t_cost)
