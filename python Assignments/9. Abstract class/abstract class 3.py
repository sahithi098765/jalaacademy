from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """An abstract class with abstract methods."""

    @abstractmethod
    def abstract_method_1(self):
        """First abstract method."""
        pass

    @abstractmethod
    def abstract_method_2(self):
        """Second abstract method."""
        pass

class ChildClass(AbstractClass):
    """A concrete subclass of the abstract class."""

    def abstract_method_1(self):
        """Implementation of the first abstract method."""
        return "ChildClass: Implementation of abstract_method_1"

    def abstract_method_2(self):
        """Implementation of the second abstract method."""
        return "ChildClass: Implementation of abstract_method_2"

    def call_abstract_methods(self):
        """Method to call the implemented abstract methods."""
        return self.abstract_method_1(), self.abstract_method_2()

# Create an instance of the child class
child_instance = ChildClass()

# Call the method that calls the abstract methods
result1, result2 = child_instance.call_abstract_methods()

# Print the results
print(result1)
print(result2)
