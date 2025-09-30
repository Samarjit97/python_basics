def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

if __name__ == "__main__":
    print("Select operation: +  -  *  /")
    op = input("Enter operation: ").strip()

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        raise SystemExit(1)

    if   op == "+": print("Result:", add(a, b))
    elif op == "-": print("Result:", subtract(a, b))
    elif op == "*": print("Result:", multiply(a, b))
    elif op == "/": print("Result:", divide(a, b))
    else:           print("Unknown operation.")
