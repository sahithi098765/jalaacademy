from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """An abstract class with abstract and non-abstract methods."""

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def abstract_method(self):
        """An abstract method that must be implemented by subclasses."""
        pass

    def non_abstract_method(self):
        """A non-abstract method that can be used by subclasses."""
        return f"Value: {self.value}"

class SubClass(AbstractClass):
    """A subclass of the abstract class."""

    def __init__(self, value, extra_value):
        super().__init__(value)
        self.extra_value = extra_value

    def abstract_method(self):
        """Implementation of the abstract method."""
        return f"Abstract method called. Extra value: {self.extra_value}"

# Create an object of the subclass
sub_object = SubClass(10, "extra")

# Access the non-abstract method through the subclass object
print(sub_object.non_abstract_method())

# Access the abstract method through the subclass object
print(sub_object.abstract_method())

#Attempting to create an object of the abstract class directly will raise an error.
try:
    abstract_object = AbstractClass(5)
except TypeError as e:
    print(f"Error: {e}")
