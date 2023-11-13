hidden = 6
guess = int(input("Enter number between 1-20 :"))
while (guess != hidden):
    print("Guess is not correct")
    guess = int(input("Enter number between 1-20 :"))
    if (guess == hidden):
        print("guess is correct.")
        break
    

