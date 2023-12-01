"""
CP1404/CP5632 Practical
Starter code for cumulative total income program

def main()
    incomes = []
    get num_months

    for month in range(1, num_months + 1)
        get income
        incomes.append(income)
    print_income_report(incomes)

def print_income_report(incomes)
    print Income Report
    total = 0
    for month, income in enumerate(incomes, start=1)
        total += income
        print Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}

main()
"""
def main():
    incomes = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)
    print_income_report(incomes)

def print_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")

main()
