class MyClass:
    def __init__(self, public_arg, protected_arg, private_arg):
        """Constructor with public, protected, and private attributes."""
        self.public_attribute = public_arg  # Public attribute
        self._protected_attribute = protected_arg  # Protected attribute
        self.__private_attribute = private_arg  # Private attribute
        print("Constructor called.")

    def public_method(self):
        print(f"Public method called. Public attribute: {self.public_attribute}")

    def _protected_method(self):
        print(f"Protected method called. Protected attribute: {self._protected_attribute}")

    def __private_method(self):
        print(f"Private method called. Private attribute: {self.__private_attribute}")

# Create an instance of the class
obj = MyClass("Public Value", "Protected Value", "Private Value")

# Access public members
obj.public_method()
print(f"Public attribute: {obj.public_attribute}")

# Access protected members (not recommended outside the class/subclasses)
obj._protected_method()
print(f"Protected attribute: {obj._protected_attribute}")

# Access private members (using name mangling)
obj._MyClass__private_method()
print(f"Private attribute: {obj._MyClass__private_attribute}")

# Attempting to access private members directly will raise an AttributeError:
# obj.__private_method()
# print(obj.__private_attribute)

# Example Subclass demonstrating protected access.
class SubClass(MyClass):
    def __init__(self, public_arg, protected_arg, private_arg, subclass_arg):
        super().__init__(public_arg, protected_arg, private_arg)
        self.subclass_arg = subclass_arg

    def access_protected(self):
        print(f"Subclass Protected attribute: {self._protected_attribute}")
        self._protected_method()

sub_obj = SubClass("Public Value", "Protected Value", "Private Value", "Subclass Value")
sub_obj.access_protected()
