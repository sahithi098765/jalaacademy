try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except OSError as e:
    print(f"IOException Occurred: {e}")
