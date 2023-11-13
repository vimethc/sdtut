import random
hidden = 6
guess = random.randint (1,20)   
while (guess != hidden):
    print(guess,'Guess is not correct.')
    guess = random.randint(1,20)
    if guess == hidden:
        print(guess,'Guess is correct.')
        break

