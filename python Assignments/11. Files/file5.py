def read_from_index(filepath, index, length=1):
    """
    Reads a specified number of bytes from a file at a given index using seek().

    Args:
        filepath (str): The path to the file.
        index (int): The index (byte offset) to start reading from.
        length (int, optional): The number of bytes to read. Defaults to 1.

    Returns:
        bytes or None: The bytes read from the file, or None if an error occurs.
    """
    try:
        with open(filepath, 'rb') as file:  # Open in binary mode
            file.seek(index)
            data = file.read(length)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
file_path = 'index_file.bin' # Replace with your file path
#create a test binary file if one does not exist.
try:
    with open(file_path, 'xb') as f:
        f.write(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
except FileExistsError:
    pass

# Read a single byte from index 5
byte_at_5 = read_from_index(file_path, 5)
if byte_at_5:
    print(f"Byte at index 5: {byte_at_5}") # Should print b'5'

# Read 3 bytes from index 10
bytes_at_10 = read_from_index(file_path, 10, 3)
if bytes_at_10:
    print(f"Bytes at index 10: {bytes_at_10}") # Should print b'ABC'

# Read from the beginning
bytes_at_0 = read_from_index(file_path, 0, 4)
if bytes_at_0:
    print(f"Bytes at index 0: {bytes_at_0}") # Should print b'0123'

# Attempt to read past the end of the file (will return fewer bytes)
bytes_at_30 = read_from_index(file_path, 30, 10)
if bytes_at_30:
    print(f"Bytes at index 30: {bytes_at_30}") #Should print b'YZ'
