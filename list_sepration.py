'''Sample List:[1, 2, 3, 4, 5, 6, 7, 8, 9]
    Expected Result: [2, 4, 6, 8]'''
list=[1,2,3,4,5,6,7,8,9]
out=[]
for i in range(0,9):
    if list[i]%2==0:
      out.append(list[i])
print('list of even numver:',out)      
