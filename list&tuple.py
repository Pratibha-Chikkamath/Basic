# X = [10,20,30] print last 2 values using : operator
x=[10,20,30]
print(x[1:])
# X = [10,20,30] print all elements using : operator
x=[10,20,30]
print(x)
# X = [10,20,30,40…100] print 10 30 50 and so on (alternative elements) without using the  for loop. Hint - use :: operator
x=[10,20,30,40,50,60,70,80,90,100]
print(x[0: :2])
# Store 10,20,30,....980,990,1000 into a list. Hint - use range
x=list(range(10,1001,10))
print(x)
# Take a list of 10 elements print elements in reverse order, hint use :: operator
x=[10,20,30,40,50,60,70,80,90,100]
print(x[ : :-1])
#Take a list of 10 elements print elements in reverse order using for loop
x=[10,20,30,40,50,60,70,80,90,100]
for i in range(-1,-1,-1):
    print(i)
# Take a list of 10 elements print all elements using for loop
x=[10,20,30,40,50,60,70,80,90,100]
for i in x:
    print(i)
# Show one eg for the property list is mutable
x=[10,20,30,40,50,60,70,80,90,100]
x[2]=200
print(x)
# Modify 2nd index element of list with 300
x=[10,20,30,40,50,60,70,80,90,100]
x[2]=300
print(x)
#. Which method do you use to search if a given element is available in the list. Show e.g.
 #how do you use it. What happens if the element is not available?
x=[10,20,30,40,50,60,70,80,90,100]
if 3000 in x:
    print("number is availbele")
else:
    print("number is not availble")
# Which method do you use to delete an element present in the list. Show one e.g. how do
# you use it.
x=[10,20,30,40,50,60,70,80,90,100]
x.remove(100)
print(x)
# Insert a new element before 1st index in the list using a method of list, show e.g. of that
 #method
x=[10,20,30,40,50,60,70,80,90,100]
x.insert(0,22)
print(x)
#. Which method do you use to delete an element present in the 1st index of the list? Show
# code
x=[10,20,30,40,50,60,70,80,90,100]
x.pop(2)
print(x)
# x=[ (10,20), (30,40), (50,60) ] print element 40
x=[ (10,20), (30,40), (50,60) ]
print(x[1][1])
#In the above example what will happen if we print(x[-1][-1])
x=[ (10,20), (30,40), (50,60) ]
print(x[-1][-1])

