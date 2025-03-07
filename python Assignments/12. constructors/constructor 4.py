class Car:
    """A class representing a car with constructor attributes."""

    def __init__(self, make, model, year, color="unknown"):
        """
        Constructor for the Car class.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The manufacturing year of the car.
            color (str, optional): The color of the car. Defaults to "unknown".
        """
        self.make = make  # Attribute: Make of the car
        self.model = model  # Attribute: Model of the car
        self.year = year  # Attribute: Year of the car
        self.color = color  # Attribute: Color of the car

        print(f"A {self.color} {self.year} {self.make} {self.model} has been created.")

    def display_car_info(self):
        """Displays the car's information."""
        print(f"Car Information:")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Year: {self.year}")
        print(f"  Color: {self.color}")

# Example Usage:

# Creating Car objects using the constructor
car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Civic", 2021)  # Color defaults to "unknown"
car3 = Car("Tesla", "Model S", 2023, "Red")

# Accessing attributes directly
print(f"\nCar1 Make: {car1.make}")
print(f"Car2 Year: {car2.year}")
print(f"Car3 Color: {car3.color}")

# Calling a method that uses attributes
print("\n")
car1.display_car_info()
print("\n")
car2.display_car_info()
print("\n")
car3.display_car_info()

#Demonstrating that attributes are instance specific.
car1.color = "Silver"
print("\nCar1 color changed.")
car1.display_car_info()
print("\nCar2 display info, to show no change.")
car2.display_car_info()
