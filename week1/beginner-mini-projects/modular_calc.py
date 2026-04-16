a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operation = input("Which calculation do you want to perform?:\na. Addition\nb. Subtraction\nc. Multiplication\nd. Division\n")


def add():
    result = a+b
    return result

def sub():
    result = a-b
    return result

def mul():
    result =a*b
    return result

def div():
    result = a/b
    return result

if operation.lower()=="addition":
    print(f"{a}+{b}={add()}")
elif operation.lower()=="subtraction":
    print(f"{a}-{b}={sub()}")
elif operation.lower()=="multiplication":
    print(f"{a}*{b}={mul()}")
elif operation.lower()=="division":
    print(f"{a}/{b}={div()}")
else:
    print("Please choose a valid operation")