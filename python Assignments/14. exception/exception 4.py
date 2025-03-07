def divide(a, b):
    return a / b
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = divide(num1, num2)
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
