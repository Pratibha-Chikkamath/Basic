fno=0
sno=1
print(fno)
print(sno)
res=fno+sno

#assume that i want to print fibonacci series upto 100
while res<100:
    print(res)
    fno=sno
    sno=res
    res=fno+sno
