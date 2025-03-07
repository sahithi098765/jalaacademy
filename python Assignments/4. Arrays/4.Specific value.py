def test(n):
    a=[]
    for i in range(n):
        k=int(input())
        a.append(k)
    m=int(input())
    if m in a:
        return True
    else:
        return False
n=int(input())
k=test(n)
print(k)
