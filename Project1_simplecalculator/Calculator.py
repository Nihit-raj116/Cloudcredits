# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y
def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter choice (1/2/3/4): "))

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    if choice == 1:
        Result= add(x, y)
    elif choice == 2:
        Result= subtract(x, y)
    elif choice == 3:
        Result= multiply(x, y)
    elif choice == 4:
        Result= divide(x, y)
    else:
        print("Invalid input. Please select 1, 2, 3, or 4.")
    print(f'result:{Result}')
main()