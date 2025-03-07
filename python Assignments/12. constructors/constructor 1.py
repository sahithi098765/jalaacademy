class MyClass:
    """A class with multiple constructors."""

    def __init__(self, arg1=None, arg2=None):
        """
        Constructor with default arguments (default constructor),
        one argument constructor, and two argument constructor.
        """
        if arg1 is None and arg2 is None:
            print("Default constructor called.")
        elif arg2 is None:
            print(f"One argument constructor called with arg1: {arg1}")
            self.arg1 = arg1
        else:
            print(f"Two argument constructor called with arg1: {arg1} and arg2: {arg2}")
            self.arg1 = arg1
            self.arg2 = arg2

class MainClass:
    """Main class to instantiate MyClass and call its constructors."""

    def __init__(self):
        """Initializes the MainClass and calls the MyClass constructors."""
        self.default_instance = MyClass()
        self.one_arg_instance = MyClass("Hello")
        self.two_arg_instance = MyClass("Hello", 123)

# Instantiate the MainClass to call the constructors
main_instance = MainClass()
