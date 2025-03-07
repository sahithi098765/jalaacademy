try:
    a=int(input())
    b=int(input())
    n=a%b
    print(n)
except ArithmeticError:
    print('cant be divided by 0')
