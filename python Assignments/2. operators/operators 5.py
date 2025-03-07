def find_larger_smaller(num1, num2):
    if num1 > num2:
        print(f"The larger number is {num1}")
        print(f"The smaller number is {num2}")
    elif num1 < num2:
        print(f"The larger number is {num2}")
        print(f"The smaller number is {num1}")
    else:
        print("Both numbers are equal.")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
find_larger_smaller(num1, num2)
