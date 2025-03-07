def count_even_odd(arr):
    even_count = sum(1 for x in arr if x % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

arr = [1, 2, 3, 4, 5]
even, odd = count_even_odd(arr)
print("Even count:", even, "Odd count:", odd)
