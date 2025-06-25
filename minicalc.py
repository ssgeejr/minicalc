# minicalc.py
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python minicalc.py <number1> <operator> <number2>")
        sys.exit(1)

    num1_str, operator, num2_str = sys.argv[1], sys.argv[2], sys.argv[3]

    # Validate both numbers are whole numbers (integers)
    if not (num1_str.isdigit() and num2_str.isdigit()):
        print("Please provide two whole numbers.")
        sys.exit(1)

    num1 = int(num1_str)
    num2 = int(num2_str)

    # Only allow specific operators
    if operator not in ['+', '-', '*', '/']:
        print("Operator must be one of: +, -, *, /")
        sys.exit(1)

    # Handle division by zero
    if operator == '/' and num2 == 0:
        print("Division by zero is not allowed.")
        sys.exit(1)

    # Perform the operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2

    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
