def write_text_to_file(filepath, input_stream):
    """
    Writes text from an input stream to a .txt file.

    Args:
        filepath (str): The path to the output .txt file.
        input_stream (iterable): An iterable that yields strings (e.g., a list of strings, a generator, or a string).
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            for chunk in input_stream:
                file.write(chunk)

    except PermissionError:
        print(f"Error: Permission denied to write to {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage with a list of strings (simulating an input stream):
file_path = 'output.txt'
input_data = ["This is line 1.\n", "This is line 2.\n", "And this is the final line."]

write_text_to_file(file_path, input_data)

#Example usage with a single string.
file_path2 = 'output2.txt'
input_data2 = "This is a single string that will be written to the file."

write_text_to_file(file_path2, [input_data2]) #Must be iterable, so put string in a list.

#Example usage with a generator (also simulating an input stream):
def generate_text():
    yield "Generator line 1.\n"
    yield "Generator line 2.\n"
    yield "Generator final line."

file_path3 = 'output3.txt'
write_text_to_file(file_path3, generate_text())

print(f"Text written to {file_path}, {file_path2}, and {file_path3}.")

#Example of using a string directly (not recommended for large strings)

def write_text_to_file_string(filepath, input_string):
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(input_string)
    except PermissionError:
        print(f"Error: Permission denied to write to {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

file_path4 = "output4.txt"
input_string = "This is a single string written directly."
write_text_to_file_string(file_path4, input_string)

print(f"Text written to {file_path4}.")
