def add(n):
    a=[]
    s=0
    for i in range(n):
        k=int(input())
        a.append(k)
    for i in a:
        s=s+i
    return s

n=int(input())
k=add(n)
print(k)
