
"""
Taxi Simulator Program
Uses Taxi and SilverServiceTaxi classes.
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
        if choice == 'q':
            break
        elif choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = input("Choose taxi: ")
            try:
                current_taxi = taxis[int(taxi_choice)]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == '__main__':
    main()
