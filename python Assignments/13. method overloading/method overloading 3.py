class MyClass:
    def my_method(self, arg1):
        """First method with one parameter (string)."""
        print(f"First method called: {arg1}")

    def my_method(self, arg1):
        """Second method with one parameter (string)."""
        print(f"Second method called: {arg1}")

# Create an instance of the class
obj = MyClass()

# Call the method
obj.my_method("Hello")

#Demonstration of how python handles this.
print(MyClass.my_method) #This shows that the second definition overwrites the first.
