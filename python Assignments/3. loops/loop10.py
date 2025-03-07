def is_palindrome(num):
    return str(num) == str(num)[::-1]  
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a Palindrome number.")
else:
    print(f"{num} is not a Palindrome number.")
