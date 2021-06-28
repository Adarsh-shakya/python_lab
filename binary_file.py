f=open('test.txt','wb')
h='my name is Adarsh shakya'
f.write(h.encode())
#f.seek(-4,2)
#print(f.tell())
f.close()