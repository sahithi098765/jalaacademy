def get_gender(choice):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    return switch.get(choice.upper(), "Invalid Input")  
choice = input("Enter M for Male or F for Female: ")
print(f"Gender: {get_gender(choice)}")
