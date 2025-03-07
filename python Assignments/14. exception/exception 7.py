def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    finally:
        print("Execution completed.")

num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
divide(num1, num2)
