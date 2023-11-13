try:
    age = input('Enter your age:  ') 
    age = int(age) 
    if age >= 18: 
            print("You can vote.") 
    else:
        print("You can't vote.")
except:
     print("Invalid input...")
        