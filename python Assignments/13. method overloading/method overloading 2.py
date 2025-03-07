class MyClass:
    def my_method(self, arg1):
        """Method with one parameter (string)."""
        if isinstance(arg1, str):
            print(f"String method called: {arg1}")
        else:
            print("String method called with non string argument.")

    def my_method(self, arg1, arg2):
        """Method with two parameters (int, float)."""
        if isinstance(arg1, int) and isinstance(arg2, float):
            print(f"Int-float method called: {arg1}, {arg2}")
        else:
            print("Int-float method called with incorrect types.")

# Create an instance of the class
obj = MyClass()

# Call the method with two parameters (int, float)
obj.my_method(10, 3.14)

# Call the method with one parameter (string)
obj.my_method("Hello")

# Calling the method with one integer will raise a TypeError.
try:
    obj.my_method(10)
except TypeError as e:
    print(f"Error: {e}")

#Demonstration of how python handles this.
print(MyClass.my_method) #This shows that the second definition overwrites the first.
