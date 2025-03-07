def find_common_elements(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
print("Common values:", find_common_elements(arr1, arr2))
