class MyClass:
    static_var = "I am a static variable"
    @classmethod
    def modify_static(cls, new_value):
        cls.static_var = new_value
print(MyClass.static_var)  
MyClass.modify_static("Changed within class")
print(MyClass.static_var)
obj1 = MyClass()
obj2 = MyClass()
print(obj1.static_var)  
print(obj2.static_var)  
