def incrementdecrement(a):
    res={}
    res["Increment"]= a+1
    res["Decrement"]= a-1
    return res
num1=int(input("Enter a value"))
print(incrementdecrement(num1))
