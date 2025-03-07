n=int(input())
a=[]
for i in range(n):
    k=int(input())
    a.append(k)
m=int(input())
if m in a:
    print(a[m-1])
else:
    print("Not in array")
    
