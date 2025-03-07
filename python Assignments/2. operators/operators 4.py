def relational_operators(num1, num2):
    print(f"{num1} < {num2} : {num1 < num2}")   # Less than
    print(f"{num1} <= {num2} : {num1 <= num2}") # Less than or equal to
    print(f"{num1} > {num2} : {num1 > num2}")   # Greater than
    print(f"{num1} >= {num2} : {num1 >= num2}") # Greater than or equal to

# Input: Take two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Demonstrate relational operators
relational_operators(num1, num2)
