from arithmetic_operations import perform_operation

def perform_operation():
    """
    This function performs an arithmetic operation based on user input.
    It prompts the user to enter two numbers and an operator, then calculates
    and returns the result of the operation.
    """
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        result = perform_operation(num1, num2, operator)
        print(f"The result of {num1} {operator} {num2} is: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")