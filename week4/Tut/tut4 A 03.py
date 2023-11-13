hidden = 6
guess = int(input("Enter number between 1-20 :"))
while (guess != hidden):
    if guess < 6:
        print("Guess is low")
        print("Guess is not correct")
    else:
        print("guess is too high")
        print("guess is not correct.")
        guess = int(input("Enter number between 1-20 :"))
if (guess == hidden):
    print("guess is correct.")
    break
    

