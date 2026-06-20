# Calculator Project - Example Solution
# This is ONE possible way to solve the calculator project.
# Your solution might look different, and that's perfectly fine!
# The important thing is that it works and uses only basic Python concepts.

def main():
    """Main function that runs the calculator program."""
    print("=" * 50)
    print("Welcome to the Simple Calculator!")
    print("=" * 50)
    print("\nSupported operations: +, -, *, /")
    print("Example: '5 + 3' or '20 / 4'")
    print("Type 'quit' to exit.\n")

    while True:
        # Get user input
        user_input = input("Enter a mathematical expression: ").strip()

        # Check if user wants to quit
        if user_input.lower() == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break

        # Skip empty input
        if not user_input:
            print("Please enter a valid expression.\n")
            continue

        # Parse the expression
        result = parse_and_calculate(user_input)

        # Display result or error message
        if result is not None:
            print(f"Result: {result}\n")
        else:
            print("Invalid expression. Please try again.\n")


def parse_and_calculate(expression):
    """
    Parse the expression and perform the calculation.

    Args:
        expression (str): User input containing the mathematical expression

    Returns:
        float or int: The result of the calculation, or None if invalid
    """
    # Strip whitespace from the expression
    expression = expression.strip()

    # List of supported operators
    operators = ["+", "-", "*", "/"]

    # Try each operator
    for operator in operators:
        if operator in expression:
            # Split the expression by the operator
            parts = expression.split(operator)

            # Check if we have exactly 2 parts
            if len(parts) == 2:
                try:
                    # Extract and strip whitespace from both parts
                    num1_str = parts[0].strip()
                    num2_str = parts[1].strip()

                    # Convert strings to numbers
                    num1 = float(num1_str)
                    num2 = float(num2_str)

                    # Perform the calculation based on the operator
                    if operator == "+":
                        result = num1 + num2
                    elif operator == "-":
                        result = num1 - num2
                    elif operator == "*":
                        result = num1 * num2
                    elif operator == "/":
                        # Check for division by zero
                        if num2 == 0:
                            print("Error: Cannot divide by zero!")
                            return None
                        result = num1 / num2

                    # Return the result as an integer if it's a whole number
                    if isinstance(result, float) and result.is_integer():
                        return int(result)
                    return result

                except ValueError:
                    # If conversion to float fails, the input is invalid
                    print("Error: Could not convert input to numbers.")
                    return None

    # If no operator was found or no valid expression was made
    print("Error: Please include one of these operators: +, -, *, /")
    return None


# Run the program
if __name__ == "__main__":
    main()
