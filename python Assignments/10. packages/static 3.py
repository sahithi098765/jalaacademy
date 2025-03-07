class MyClass:
    static_var = "I am a static variable"
    def __init__(self, value):
        self.instance_var = value  
    def modify_static(self, new_value):
        MyClass.static_var = new_value
obj1 = MyClass("Instance 1")
obj1.modify_static("Changed from instance")
obj2 = MyClass("Instance 2")
print(obj1.static_var)  
print(obj2.static_var)  
print(MyClass.static_var)  
