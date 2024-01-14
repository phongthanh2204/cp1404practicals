
""" 
Test for Unreliable Car class
"""

from unreliable_car import UnreliableCar

def main():
    # Create instances of UnreliableCar
    reliable_car = UnreliableCar('Reliable', 100, 90)  # High reliability
    unreliable_car = UnreliableCar('Unreliable', 100, 10)  # Low reliability

    # Test driving the cars
    for i in range(1, 6):
        print(f"Attempt {i}: Reliable car drove {reliable_car.drive(30)}km")
        print(f"Attempt {i}: Unreliable car drove {unreliable_car.drive(30)}km")

if __name__ == '__main__':
    main()
