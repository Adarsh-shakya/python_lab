#print max and min value of dict
dct={2:4,8:6,3:6,9:0,6:5,1:3}
l=list(dct.values())
l.sort()
print('max',l[-1])
print('min',l[0])
