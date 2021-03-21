#check anagram string ex.  LISTEN=SILENT
str1=input("enter the string: ")
str2=input("enter the string: ")
s2=list(str2)
s1=list(str1)
s2.sort()
s1.sort()
if s1==s2:
    print("string is anagram")
else:
    print("string is not anagram")
