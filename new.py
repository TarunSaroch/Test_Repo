import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return x ** y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

print("Welcome to the Scientific Calculator!")

while True:
    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("0. Exit")

    choice = input("Enter choice (0-9): ")

    if choice == '0':
        print("Exiting the calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if choice in ('1', '2', '3', '4', '6'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter the number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")

    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

    elif choice == '5':
        print(f"Square root of {num1} = {square_root(num1)}")

    elif choice == '6':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")

    elif choice == '7':
        print(f"Sin({num1} degrees) = {sin(num1)}")

    elif
