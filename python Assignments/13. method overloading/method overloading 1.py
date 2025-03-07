class MyClass:
    def my_method(self, arg1):
        """Method with one parameter."""
        print(f"Method with one parameter called: {arg1}")

    def my_method(self, arg1, arg2):
        """Method with two parameters."""
        print(f"Method with two parameters called: {arg1}, {arg2}")

# Create an instance of the class
obj = MyClass()

# Call the method with two parameters
obj.my_method("Hello", "World")

# Calling with only one parameter will raise a TypeError.
try:
    obj.my_method("Only one argument")
except TypeError as e:
    print(f"Error: {e}")

# Demonstration of how python handles this.
print(MyClass.my_method) # This shows that the second definition overwrites the first.
