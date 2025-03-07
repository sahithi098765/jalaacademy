def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

arr = [1, 2, 3, 4, 5, 2, 3]
print("Duplicate values:", find_duplicates(arr))
