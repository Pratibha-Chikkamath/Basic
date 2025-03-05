#find biggest element in a list
mylist=[10,9,11,23,8]
big=mylist[0]
for item in mylist:
    if big<item:
        big=item
print("biggest is...",big)