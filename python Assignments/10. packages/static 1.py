class MyClass:
    static_var = "I am a static variable"
    def __init__(self, value):
        self.instance_var = value 
print(MyClass.static_var)
obj = MyClass("Instance Value")
print(obj.static_var) 
MyClass.static_var = "New static value"
print(obj.static_var) 
obj.static_var = "Changed from instance"
print(obj.static_var)  
print(MyClass.static_var)  
