class RandomAccessFileReader:
    """
    A class for reading a file with random access capabilities.
    """

    def __init__(self, filepath):
        """
        Initializes the RandomAccessFileReader.

        Args:
            filepath (str): The path to the file.
        """
        self.filepath = filepath
        self.file = None
        try:
            self.file = open(self.filepath, 'rb')  # Open in binary mode for random access
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
        except PermissionError:
            print(f"Error: Permission denied to read {filepath}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def read_chunk(self, offset, size):
        """
        Reads a chunk of data from the file at a specific offset.

        Args:
            offset (int): The offset (in bytes) to start reading from.
            size (int): The size of the chunk to read (in bytes).

        Returns:
            bytes: The chunk of data read from the file, or None if an error occurs.
        """
        if self.file is None:
            return None

        try:
            self.file.seek(offset)
            chunk = self.file.read(size)
            return chunk
        except Exception as e:
            print(f"Error reading chunk: {e}")
            return None

    def close(self):
        """
        Closes the file.
        """
        if self.file:
            self.file.close()
            self.file = None

# Example usage:
file_path = 'random_access_file.bin' # Replace with your file path
#create a test binary file if one does not exist.
try:
    with open(file_path, 'xb') as f:
        f.write(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
except FileExistsError:
    pass

reader = RandomAccessFileReader(file_path)

if reader.file: #only run the example if the file opened correctly.
    chunk1 = reader.read_chunk(5, 10)  # Read 10 bytes starting from offset 5
    if chunk1:
        print(f"Chunk 1: {chunk1}") #Should print b'56789ABCDE'

    chunk2 = reader.read_chunk(20, 5)  # Read 5 bytes starting from offset 20
    if chunk2:
        print(f"Chunk 2: {chunk2}") #Should print b'KLMNO'

    chunk3 = reader.read_chunk(0, 4) #Read from the beginning.
    if chunk3:
        print(f"Chunk 3: {chunk3}") #Should print b'0123'

    reader.close() #Important to close the file
