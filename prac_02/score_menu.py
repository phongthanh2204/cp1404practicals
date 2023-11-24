"""
def get_valid_score
    get score
    while score < 0 or score > 100
        print Invalid score
        get score
    return score

def determine_result
    if score < 0 or score > 100
        return Invalid score
    elif score >= 90
        return Excellent
    elif score >= 50
        return Passable
    else return bad

def show_starts
    print '*' * score

def main
    score = get_valid_score

    MENU = (G)et a valid score
(P)rint result
(S)how stars
(Q)uit
    display MENU
    get choice
    while choice != Q
        if choice == G
            score = get_valid_score
        elif choice == P
            result = determine_result
            print result
        elif choice == S
            show_stars
        else
            print Invalid choice
        display MENU
        get choice
    print Farewell!

main
"""
def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print('*' * int(score))

def main():
    score = get_valid_score()

    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell!")

if __name__ == "__main__":
    main()
