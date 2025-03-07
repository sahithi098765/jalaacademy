def insert_element(arr, elem, pos):
    arr.insert(pos, elem)
    return arr

arr = [1, 2, 3, 4, 5]
print("Array after inserting 10 at index 2:", insert_element(arr, 10, 2))
