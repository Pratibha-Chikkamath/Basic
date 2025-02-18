def m1(f):
    x=f(5)
    print(x)
f1=lambda x:x**2
m1(f1)

sum_lambda = lambda a, b, c: a + b + c
result = sum_lambda(5, 10, 15)
print(result)

biggestno=lambda a,b,c:a if a>b and a>c  else b
result=biggestno(33,4,5)
print(result)

l1=[10,5,6,8]
l2=list(map(lambda x:x+1,l1))
print(l2)

l1=[10,11,12,13,14,15,16,17,18,19,20]
l2=list(filter(lambda x:x%2==0,l1))
print(l2)

l1=[10,11,1,13,14,15,16,8,18,9,20]
l2=list(filter(lambda x:x>10,l1))
print(l2)
