# minicalc.py
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python minicalc.py <number1> <number2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Please provide valid numbers.")
        sys.exit(1)

    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

if __name__ == "__main__":
    main()
