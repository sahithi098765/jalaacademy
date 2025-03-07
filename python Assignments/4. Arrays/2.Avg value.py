def avg(n):
    a=[]
    s=0
    for i in range(n):
        k=int(input())
        a.append(k)
    for i in a:
        s=s+i
    return s//n
n=int(input())
k=avg(n)
print(k)
