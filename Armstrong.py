num=int(input("enter a number:"))
temp=num
result=0
while num>0:
    last=num%10
    num=num//10
    result=result+(last*last*last)
print("sum of cude is ",result)
if result==temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not  armstrong number")
