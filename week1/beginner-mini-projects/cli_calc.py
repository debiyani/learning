a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
calc = input('Which arithematic calculation do you want to perform? \n a.Addition \n b.Subtraction \n c.Multipliction \n d.Division \n')
if calc == 'a':
    sum=a+b
    print(f"The sum of {a} and {b} is {sum}.")
elif calc == 'b':
    sub=a-b
    print(f"The difference of {a} and {b} is {sub}.")
elif calc == 'c':
    mul=a*b
    print(f"The multiplication of {a} and {b} is {mul}.")
elif calc =='d':
    div=a/b
    print(f"{a}/{b} equals {div}.")
else:
    print("Invalid operation.")