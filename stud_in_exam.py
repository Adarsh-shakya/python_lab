TA=int(input('Enter the total number class held: '))
AA=int(input('Enter the number of class attended: '))
percant=(TA/100)*AA
if percant>75:
    print('total present',percant)
    print('student will allowed to sit in exam')
else:
    print('total present',percant)
    print('student will not sit in  exam')

