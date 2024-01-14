
""" 
Unreliable Car class
Derived from Car class with additional unreliability feature.
"""

import random
from prac_09.car import Car

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """ Initialize an UnreliableCar instance, based on parent class Car. """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """ Drive the car if a random number is less than the car's reliability. """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0

# Testing if the code works as expected (will be removed in the final file)
if __name__ == '__main__':
    test_car = UnreliableCar('Test', 100, 50)
    print(test_car.drive(30))  # Random outcome
