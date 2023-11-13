x = int(input('Give me a number:'))
if x < 0:
    print(x,"is negative")
else:
    print(x,"is positive")

    print("-----------------------------------------------------------")


def add(x,y):
    return x + y
def subtract(x, y):
    return x - y
def multiplication(x,y):
    return x * y
def devision(x,y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

print("Operators.\n1. Add.\n2. Subtract.\n3. Multiply.\n4. Divide.")

while True:
    choice = input("Enter choice (1/2/3/4)")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter 1st number:"))
        num2 = float(input("Enter 2nd number:"))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1,num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiplication(num1,num2)}")
        
        elif choice == '4':
            print(f"{num1} - {num2} = {devision(num1,num2)}")
    
        break
    else:
        print("Invalid input.")


        
