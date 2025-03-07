def read_text_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file: #Using utf-8 encoding is recommended
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read {filepath}")
        return None
    except Exception as e: #Catching other potential errors
        print(f"An unexpected error occurred: {e}")
        return None
file_path = 'my_text_file.txt' 
try:
    with open(file_path, 'x', encoding='utf-8') as f:
        f.write("This is a test file.\nIt has multiple lines.\nAnd some example text.")
except FileExistsError:
    pass 

file_content = read_text_file(file_path)

if file_content is not None:
    print("File content:")
    print(file_content)


def read_text_file_lines(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

lines = read_text_file_lines(file_path)

if lines is not None:
    print("\nFile content, line by line:")
    for line in lines:
        print(line.strip())
