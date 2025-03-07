def generate_arithmetic_exception():
    result = 10 / 0  

try:
    generate_arithmetic_exception()
except ZeroDivisionError as e:
    print(f"Arithmetic Exception Occurred: {e}")
