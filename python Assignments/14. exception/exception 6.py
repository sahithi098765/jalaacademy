class AgeTooLowError(Exception):
    def __init__(self, message="Age must be 18 or above to proceed!"):
        super().__init__(message)

def check_age(age):
    if age < 18:
        raise AgeTooLowError()
    else:
        print("Access granted.")

try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except AgeTooLowError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
