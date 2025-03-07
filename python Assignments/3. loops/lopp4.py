n=int(input())
print("Even Numbers:")
for num in range(1, n):
    if num % 2 == 0:
        print(num, end=" ")
print("\nOdd Numbers:")
for num in range(1,n):
    if num % 2 != 0:
        print(num, end=" ")
