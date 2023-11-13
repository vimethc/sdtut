

try:
    brand = str(input("Enter your water bottle brand:")).lower()
    size = float(input("Enter the size of water bottle: "))

    if brand == "aqual" and size == 750:
        print("Get")
    else:
        print("Go home")
except ValueError:
    print("invalid input.Enter valid inputs")
