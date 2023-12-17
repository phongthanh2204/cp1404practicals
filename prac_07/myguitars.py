
from guitar import Guitar

def read_guitars_from_csv(file_path):
    guitars = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    return guitars

def guitars.sort()
    display_guitars(guitars):
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

def main():
    file_path = 'guitars.csv'
    guitars = read_guitars_from_csv(file_path)
    guitars.sort()
    display_guitars(guitars)

if __name__ == '__main__':
    main()


def get_new_guitar():
    name = input("Name: ")
    if not name:
        return None
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    return Guitar(name, year, cost)

def add_new_guitars(guitars):
    print("Enter your guitars:")
    while True:
        guitar = get_new_guitar()
        if guitar:
            guitars.append(guitar)
        else:
            break

def save_guitars_to_csv(guitars, file_path):
    with open(file_path, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    file_path = 'guitars.csv'
    guitars = read_guitars_from_csv(file_path)
    guitars.sort()
    display_guitars(guitars)
    add_new_guitars(guitars)
    save_guitars_to_csv(guitars, file_path)

main()
