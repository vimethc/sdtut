print("Let's play Guess the word")

secret=input("secret word:")

print("You have" ,len(secret)," turns to guess the word!")

word="_ "*len(secret)
print(word)
x=word.split(" ")

def fill():
    for j in range(len(secret)):
         print (x[j],end="")

missed=len(secret)

y=list(secret)
for i in range(len(secret)+1):
    
    if(missed == 0):
        print ("\n")
        print("********You Won********")
        break

    else:
        print ("\n") 
        guess=input("Enter guess:")
        
        if(guess in secret):
            missed=missed-1
            
            if(guess==y[0]):
                x[0]=y[0]
                fill()
            elif(guess==y[1]):
                x[1]=y[1]
                fill()
            elif(guess==y[2]):
                x[2]=y[2]
                fill()
            elif(guess==y[3]):
                x[3]=y[3]
                fill()
            elif(guess==y[4]):
                x[4]=y[4]
                fill()
            elif(guess==y[5]):
                x[5]=y[5]
                fill()
            elif(guess==y[6]):
                x[6]=y[6]
                fill()
            elif(guess==y[7]):
                x[7]=y[7]
                fill()
            elif(guess==y[8]):
                x[8]=y[8]
                fill()
            elif(guess==y[9]):
                x[9]=y[9]
                fill()
            elif(guess==y[10]):
                x[10]=y[10]
                fill()
            elif(guess==y[3]):
                x[3]=y[3]
                fill()
            elif(guess==y[11]):
                x[11]=y[11]
                fill()
            elif(guess==y[12]):
                x[12]=y[12]
                fill()
            elif(guess==y[13]):
                x[13]=y[13]
                fill()
            elif(guess==y[14]):
                x[14]=y[14]
                fill()
            elif(guess==y[15]):
                x[15]=y[15]
                fill()
        else:
            fill()
    
        
print ("\n") 
print("End of Game")
