n = input("Give me a number over 100:")

try:
    n = int(n)
    if n <= 100:
        print(n,'is not over.')
    else:
        print(n,"is over number.")
except ValueError:
    print("Invalid input......")


print("-----------------------------------------------------")


print("second code....")
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero!"


print("This is simple calculator....")
print("""Operators.
      1. Add.
      2. Subtract.
      3. Multiply.
      4. Divide.     """)

while True:
    choice = input("Enter choice (1 / 2 / 3 / 4):")

    if choice in( '1' , '2' , '3' , '4' , '5'):
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(f"You told add this numbers {num1} + {num2}. Answer is {add(num1, num2)}")
        
        elif choice == '2':
            print(f"You told subtract this numbers {num1} - {num2}. Answer is {subtract(num1, num2)}")

        elif choice == '3':
            print(f"You told multiply this numbers {num1} * {num2}. Answer is {multiplication(num1, num2)}")

        elif choice == '4':
            print(f"You told divide this numbers {num1} / {num2}. Answer is {division(num1, num2)}")
            
        break

    else:
        print("Invalid input...")
        
