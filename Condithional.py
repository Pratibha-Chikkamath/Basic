num=int(input("enter a number:"))
if num%3==0:
    print("Fizz")
elif num%5==0:
    print("buzz")
elif num%3==0 and num%5==0:
    print("FizzBuzz")
else:
    print(num)