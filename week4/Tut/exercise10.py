import random
hidden = random.randint(1,20)

for i in range(5):
    guess_number = int(input('Enter number:'))
    if guess_number < hidden:
        print("Lower than their guess.")
    elif guess_number > hidden:
        print("Higher than their number.")
    else:
        print("Correct guess.")
print(f"Hidden number is {hidden}")
