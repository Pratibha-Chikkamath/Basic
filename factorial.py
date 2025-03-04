#ask to user enter a number  to find factorial of it
num=int(input("enter a number:"))
res=1
for i in range(num,1,-1):
    res=res*i
print("factorial of ",num,"is",res)

