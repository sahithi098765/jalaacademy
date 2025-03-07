def check_equal(num1, num2):
    if num1 == num2:
        return True
    else:
        return False
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if check_equal(num1, num2):
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
