def contains_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

arr = [12, 23, 34, 45]
print("Contains 12 and 23:", contains_elements(arr, 12, 23))
