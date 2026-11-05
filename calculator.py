"""A simple command-line calculator for the four basic arithmetic operations."""


def calculate(first: float, operator: str, second: float) -> float:
    """Return the result of applying operator to the two numbers."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first / second
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main() -> None:
    try:
        first = float(input("Enter the first number: "))
        operator = input("Choose an operation (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
        result = calculate(first, operator, second)
    except ValueError as error:
        print(f"Error: {error}")
        return
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        return

    print(f"Result: {result:g}")


if __name__ == "__main__":
    main()