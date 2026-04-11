import random
num = int(input('Enter your guess:'))
num_to_guess = random.randint(1,100)
while num != num_to_guess:
    if num > num_to_guess:
        print(f"Number is smaller than {num}")
    elif num<num_to_guess:
        print(f"Number is greater than {num}")
    ask = input("Do you want to try again?: yes/no \n")    
    if ask.lower() == "yes":
        num = int(input('Enter your guess:'))
    else:
        print("Thank you for trying this game.")
        break
while num == num_to_guess :
    print("Wow! you guesses it. \n ............😊😊😊............")
    break