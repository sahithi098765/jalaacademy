def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above to proceed!")
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as e:
    print(f"Error: {e}")
