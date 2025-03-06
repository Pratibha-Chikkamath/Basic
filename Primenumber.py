#prime number program


num=int(input("Enter a number:"))
isprime=True
for i in range(2,num):
    if num%i==0:
        isprime=False
        break
if isprime==True:
    print(num,"is prime number")
else:
    print(num,"is not prime number")