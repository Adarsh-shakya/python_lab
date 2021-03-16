# tank problem
t=int(input("enter time in mint."))
r=5 #r of tank
h=10 #h of tank
rt=10 #rate of flow of water
v_water=t*rt
v_tank=3.14*r**2*h
if v_tank<v_water:
    print("over flow")
elif v_tank>v_water:
    print("under flow")
else:
    print("tank full filed")
