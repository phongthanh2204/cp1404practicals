
"""
Band class for CP1404
Represents a band composed of musicians with their instruments.
"""

class Band:
    def __init__(self, name):
        """ Initialize a Band with a name and an empty list of musicians. """
        self.name = name
        self.musicians = []

    def add(self, musician):
        """ Add a musician to the band. """
        self.musicians.append(musician)

    def __str__(self):
        """ Return a string representation of the band. """
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def play(self):
        """ Simulate playing of each musician in the band. """
        for musician in self.musicians:
            if musician.instruments:
                for instrument in musician.instruments:
                    print(f"{musician.name} is playing: {instrument}")
            else:
                print(f"{musician.name} needs an instrument!")

