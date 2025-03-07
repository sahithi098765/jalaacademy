def find_second_largest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr[-2] if len(unique_arr) > 1 else None

arr = [1, 2, 3, 4, 5]
print("Second largest number:", find_second_largest(arr))
