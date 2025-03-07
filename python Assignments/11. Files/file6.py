import os

def check_file_permissions(filepath):
    """
    Checks if a file has read and write permissions.

    Args:
        filepath (str): The path to the file.

    Returns:
        tuple: A tuple containing (read_access, write_access, file_exists).
               read_access and write_access are booleans, and file_exists is a boolean.
    """
    read_access = os.access(filepath, os.R_OK)
    write_access = os.access(filepath, os.W_OK)
    file_exists = os.path.exists(filepath)
    return read_access, write_access, file_exists

# Example usage:
file_path = 'permissions_test.txt'

# Create a dummy file for testing (if it doesn't already exist)
if not os.path.exists(file_path):
    try:
        with open(file_path, 'w') as f:
            f.write("Test file for permissions.")
    except Exception as e:
        print(f"Error creating test file: {e}")
        exit()

read_permission, write_permission, file_existence = check_file_permissions(file_path)

if file_existence:
    print(f"File '{file_path}' exists.")
    print(f"Read access: {read_permission}")
    print(f"Write access: {write_permission}")
else:
    print(f"File '{file_path}' does not exist.")

# Example to demonstrate a file without write access (on Unix-like systems)
# This example will likely fail on Windows, as it doesn't support fine-grained permissions in the same way.
if os.name == 'posix': #only run on linux/mac.
    try:
        os.chmod(file_path, 0o444)  # Make the file read-only
        read_permission, write_permission, file_existence = check_file_permissions(file_path)
        print(f"\nAfter making '{file_path}' read-only:")
        print(f"Read access: {read_permission}")
        print(f"Write access: {write_permission}")
        os.chmod(file_path, 0o644) # restore write permission
    except Exception as e:
        print(f"Error changing permissions: {e}")
