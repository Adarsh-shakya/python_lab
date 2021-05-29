#find the same key in two dict
d1={'key1': 1, 'key2': 3, 'key3': 2}
d2={'key1': 1, 'key2': 2}
l1=list(d1.items())
l2=list(d2.items())
for i in l1:
    for j in l2:
        if i==j:
            print(i)
