#Remove empty tuple
l=[(),(3,4,5),(),(2,3),(),(4,5),(),(2,3,4)]
for i in l:
    if len(i)==0:
        l.remove(i)
print(l)
