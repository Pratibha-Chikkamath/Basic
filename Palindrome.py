num=int(input("enter a number:"))
temp=num
rev=0
while num>0:
    last=num%10
    num=num//10
    rev=(rev*10)+last
print("reversed numbers is ",rev)
if rev==temp:
    print(temp,"is palindrome")
else:
    print(temp,"is not palindrome")
