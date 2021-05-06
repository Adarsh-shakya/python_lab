#calculate simple interest by using function
#Time by default=2 year
#Rate by default=0.10
def interest(principal,time =2,rate=0.10):
    return principal*time*rate
#__main__
prin=float(input('enter the number:  '))
print("simple insterst with default ROI and time : ")
print("Rs.",interest(prin))
