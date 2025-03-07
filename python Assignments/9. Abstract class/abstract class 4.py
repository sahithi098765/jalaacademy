from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """An abstract class with abstract and non-abstract methods."""

    @abstractmethod
    def abstract_method(self):
        """An abstract method."""
        pass

    def non_abstract_method_1(self):
        """A non-abstract method."""
        return "AbstractClass: Non-abstract method 1"

    def non_abstract_method_2(self):
        """Another non-abstract method."""
        return "AbstractClass: Non-abstract method 2"

class ChildClass(AbstractClass):
    """A concrete subclass of the abstract class."""

    def abstract_method(self):
        """Implementation of the abstract method."""
        return "ChildClass: Implementation of abstract_method"

    def call_non_abstract_methods(self):
        """Method to call non-abstract methods from the parent class."""
        return self.non_abstract_method_1(), self.non_abstract_method_2()

# Create an instance of the child class
child_instance = ChildClass()

# Call the method that calls the non-abstract methods
result1, result2 = child_instance.call_non_abstract_methods()

# Print the results
print(result1)
print(result2)
