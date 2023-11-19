print("Let's play Guess the word")
print("You have 6 turns to guess the word!")

word="_ _ _ _ _"
print(word)
x=word.split(" ")

def fill():
    for j in range(5):
         print (x[j],end="")

missed=5
secret="water"
for i in range(6):
    
    if(missed == 0):
        print ("\n")
        print("********You Won********")
        break

    else:
        print ("\n") 
        guess=input("Enter guess:")
        
        if(guess in secret):
            missed=missed-1
            
            if(guess=='w'):
                x[0]='w'
                fill()
            elif(guess=='a'):
                x[1]='a'
                fill()
            elif(guess=='t'):
                x[2]='t'
                fill()
            elif(guess=='e'):
                x[3]='e'
                fill()
            elif(guess=='r'):
                x[4]='r'
                fill()
        else:
            fill()
    
        
print ("\n") 
print("End of Game")

