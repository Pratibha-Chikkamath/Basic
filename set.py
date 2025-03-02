#create empty set
set=set()
print(type(set))
#Store 10,20,30 in a set and print 10 using index
#s = {10, 20, 30}
#print(s[0])  # ❌ This will raise a TypeError: 'set' object is not subscriptable
# Print set elements using for loop
set={10,21,39,40}
for i in set:
    print(i)
# Set stores elements in insertion order [t/f]
#false
#Sets are faster compared to lists [t/f]
#true
# Which method do you use to add a new element into the set? Show eg
set={10,21,39,40,55}
set.add(44)
print(set)
# Which method do you use to delete an element from a set? Show eg
set={10,21,39,40,55}
set.remove(40)
print(set)