import re
# Write code to find if a given text starts with word palle

s="Palle Technology python"
A="he as a gold goo"
a=(re.findall("^Palle",s))# Write code to find if a given text starts with word palle

b=(re.findall("python$",s))#Write code to find if a given text ends with word python
c=(re.findall("^Palle.*python$",s))# Write code to find if a given text starts with palle and ends with python and in between 0
 #or more letters
d=len(re.findall("\d",A)) #Find how many digits are there in a given text
e=len(re.findall("[a-z]",s))# Find how many small letters are there and how many capital letters are there in a given
 #text
h=len(re.findall("[A-Z]",s))
f=(re.findall("^he.+o$",A))# In a given text print all words starting with he and ending with o, and in the middle it has
# 1 or more letters.
g=(re.search("^he.*o$",A))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)