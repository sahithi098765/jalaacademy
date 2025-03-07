def read_file_stream(filepath, chunk_size=4096):
    """
    Reads a file in chunks, simulating a file stream.

    Args:
        filepath (str): The path to the file.
        chunk_size (int): The size of each chunk to read (in bytes).
    Yields:
        bytes: A chunk of data read from the file.
    """
    try:
        with open(filepath, 'rb') as file:  # Open in binary mode ('rb')
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except PermissionError:
        print(f"Error: Permission denied to read {filepath}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
file_path = 'large_file.bin'  # Replace with your file path.
#create a test binary file if one does not exist.
try:
    with open(file_path, 'xb') as f:
        f.write(b"This is a test binary file.\nIt has multiple lines.\nAnd some example text.")
except FileExistsError:
    pass

for chunk in read_file_stream(file_path):
    # Process each chunk of data
    print(f"Read chunk: {chunk}")
    # Example: convert bytes to string (if it's text)
    try:
        text_chunk = chunk.decode('utf-8') #try decoding as UTF-8
        print(f"Decoded chunk: {text_chunk}")
    except UnicodeDecodeError:
        print("Chunk is not valid UTF-8 text.")
    # Example: write chunk to another file
    try:
        with open("output_chunk.bin", "ab") as f: #append binary
            f.write(chunk)
    except Exception as e:
        print(f"Error writing chunk to file: {e}")

#Example of reading a large file, and only doing something with the first chunk.
def read_first_chunk(filepath, chunk_size=4096):
    try:
        with open(filepath, 'rb') as file:
            chunk = file.read(chunk_size)
            if chunk:
                return chunk
            else:
                return None
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

first_chunk = read_first_chunk(file_path)

if first_chunk:
    print(f"First chunk: {first_chunk}")
