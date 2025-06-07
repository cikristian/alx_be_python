from arithmetic_operations import perform_operation

def perform_operation():
   num1 = float(input("Enter first number: "))
   num2 = float(input("Enter second number: "))
   operation = input("Enter operation (+, -, *, /): ") 
    if operation == "+":
         result = num1 + num2
    elif operation == "-":
         result = num1 - num2
    elif operation == "*":
         result = num1 * num2
    elif operation == "/":
         if num2 != 0:
              result = num1 / num2
         else:
              return "Error: Division by zero is not allowed."
    else:
         return "Error: Invalid operation."