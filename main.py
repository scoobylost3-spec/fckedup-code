import calculator

def main():
    print("Welcome to the Buggy Calculator!")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = calculator.add(num1 num2)  # Bug: Missing comma between arguments
    elif operation == '-':
        result = calculator.subtract(num1, num2)
    elif operation == '*':
        result = calculator.multiply(num1, num2)
    elif operation == '/':
        result = calculator.divide(num1, num2)
    else:
        print("Invalid operation")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
