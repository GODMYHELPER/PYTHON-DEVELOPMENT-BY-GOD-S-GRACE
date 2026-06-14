while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sign = input("Enter sign (+,-,*,/) or q to quit:")

    if sign == "q":
        print("Calculator stopped")
        break

    if sign == "+":
        print("Result =", a+b)
elif sign == "-":
    print("Result =", a-b)
elif sign == "*":
    print("Result =", a*b)
elif sign == "/":
    if b != 0:
        print("Result =", a/b)
    else:
        print("A number can't be divided by zero")
else:
    print("Invalid operator.")