
"""
Test for SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    # Create an instance of SilverServiceTaxi
    fancy_taxi = SilverServiceTaxi('Luxury Sedan', 100, 2)  # Fanciness of 2

    # Start a fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Print details and fare
    print(fancy_taxi)
    print(f"Total fare for 18 km: ${fancy_taxi.get_fare():.2f}")  # Expected fare: $48.78

if __name__ == '__main__':
    main()
