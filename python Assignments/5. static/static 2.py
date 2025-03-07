class MyClass:
    static_var = "I am a static variable"
    def __init__(self, value):
        self.instance_var = value  
obj = MyClass("Instance Value")
print(obj.static_var)  
