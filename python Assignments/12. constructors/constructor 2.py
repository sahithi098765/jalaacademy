class SuperClass:
    """A superclass with default and argument constructors."""

    def __init__(self, arg=None):
        if arg is None:
            print("SuperClass: Default constructor called.")
        else:
            print(f"SuperClass: Argument constructor called with arg: {arg}")
            self.arg = arg

class ChildClass(SuperClass):
    """A child class that calls superclass constructors."""

    def __init__(self, child_arg=None, super_arg=None):
        """ChildClass constructor."""

        if super_arg is None:
            super().__init__()  # Call superclass default constructor
        else:
            super().__init__(super_arg)  # Call superclass argument constructor

        if child_arg is None:
            print("ChildClass: Default constructor called.")
        else:
            print(f"ChildClass: Argument constructor called with child_arg: {child_arg}")
            self.child_arg = child_arg

# Example usage:

# Call superclass default constructor from child class
child1 = ChildClass()

# Call superclass argument constructor from child class
child2 = ChildClass(child_arg="Child Value", super_arg="Super Value")

#Call child class argument constructor, but super class default constructor.
child3 = ChildClass(child_arg="Child value only")
