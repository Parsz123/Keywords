a = int(input("Enter a number for the pattern to go up to. "))

for x in range(a + 1):
    if x % 20 == 0:
        print("Twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)
