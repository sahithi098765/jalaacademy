def check_even_odd(num):
    switch = {
        0: "Even",  
        1: "Odd"    
    }
    return switch[num % 2]  
num = int(input("Enter a number: "))
print(f"{num} is {check_even_odd(num)}.")
