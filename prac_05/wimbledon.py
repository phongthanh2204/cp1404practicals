"""
Wimbledon Data Processing
Estimate: 25 minutes
Actual: 23 minutes

def main()
    filename = 'wimbledon.csv'
    data = read_data(filename)
    champions = count_champions(data)
    countries = get_countries(data)
    display_results(champions, countries)

def read_data(filename)
    with open(filename, "r", encoding="utf-8-sig") as in_file
        data = [line.strip().split(',') for line in in_file if line.strip()]
    return data

def count_champions(data)
    champions = {}
    for record in data
        name = record[1]
        champions[name] = champions.get(name, 0) + 1
    return champions

def get_countries(data)
    countries = set(record[2] for record in data)
    return sorted(countries)

def display_results(champions, countries):
    print Wimbledon Champions:
    for champion, count in champions.items()
        print {champion} {count}

    countries_str = ', '.join(countries)
    print These {len(countries)} countries have won Wimbledon:
    print(countries_str)

main()
"""
def main():
    filename = 'wimbledon.csv'
    data = read_data(filename)
    champions = count_champions(data)
    countries = get_countries(data)
    display_results(champions, countries)

def read_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        data = [line.strip().split(',') for line in in_file if line.strip()]
    return data

def count_champions(data):
    champions = {}
    for record in data:
        name = record[1]
        champions[name] = champions.get(name, 0) + 1
    return champions

def get_countries(data):
    countries = set(record[2] for record in data)
    return sorted(countries)

def display_results(champions, countries):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    countries_str = ', '.join(countries)
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(countries_str)

main()
