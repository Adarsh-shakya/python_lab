# Find key enter by the user is character ,digits or special symbol
n=input("Enter any key: ")
if n>='a' and n<='z':
    print("You entered lower case")
elif n>='A'and n<='Z':
    print("You entered upper case")
elif n>='0' and n<='9':
    print('You entered digit')
else:
    print("You entered special  symbol ")
