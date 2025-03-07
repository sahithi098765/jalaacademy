def remove_element(arr, elem):
    return [x for x in arr if x != elem]

arr = [1, 2, 3, 4, 5]
print("Array after removing 3:", remove_element(arr, 3))
