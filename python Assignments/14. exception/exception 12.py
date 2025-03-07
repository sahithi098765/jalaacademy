class MyClass:
    def __init__(self):
        self.name = "Pujitha"

try:
    obj = MyClass()
    print(obj.non_existent_field)  
except AttributeError as e:
    print(f"NoSuchFieldException Occurred: {e}")
