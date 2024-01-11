
""" 
Silver Service Taxi class
Derived from Taxi class with additional fanciness and flagfall features.
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # Class variable for flagfall

    def __init__(self, name, fuel, fanciness):
        """ Initialize a SilverServiceTaxi instance, based on parent class Taxi. """        
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """ Calculate and return the fare for the silver service taxi trip. """
        return super().get_fare() + self.flagfall

    def __str__(self):
        """ Return a string representation of the silver service taxi. """
        return f"{super().__str__()}, {self.price_per_km:.2f}/km plus flagfall of ${self.flagfall}"

# Testing if the code works as expected (will be removed in the final file)
if __name__ == '__main__':
    test_taxi = SilverServiceTaxi('Hummer', 200, 4)
    print(test_taxi)  # Should include flagfall in the string representation
