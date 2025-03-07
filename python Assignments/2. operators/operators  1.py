def arithmetic_operations(a,b):
    res={}
    res["Addition"]=a+b
    res["subtraction"]=a-b
    res["Multiplication"]=a*b
    if b != 0:
        res["division"] = a / b
    else:
        res["division"] = None 
        print("Error")
    return res
num1=int(input('enter a value'))
num2=int(input('enter b value'))
res=print(arithmetic_operations(num1,num2))
