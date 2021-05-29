#Create a dict by using two list
lst1=['name','Roll.no','address','std']
lst2=['Adarsh','01','GLA','B.tech']
dct={}
for i in range(len(lst1)):
    dct[lst1[i]]=lst2[i]
print(dct)    
