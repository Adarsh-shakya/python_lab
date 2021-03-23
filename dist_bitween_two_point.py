# Find the distance bitween two point
x1, y1 = input("Enter the frist point: ").split()
x2, y2 = input("Enter the second point: ").split()

d=((int(x1)-int(x2))**2+(int(y1)-int(y2))**2)**0.5
print("Distance bitween two point is",d)
