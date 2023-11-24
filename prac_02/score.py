"""
import random

def main
    get user_score
    result = determine_result
    print result
    random_score = random.uniform
    print random_score
    random_result = determine_result
    print random_result'

def determine_result
    if score < 0 or score > 100
        return Invalid score
    elif score >= 90
        return Excellent
    elif score >= 50
        return Passable
    else return bad

main
"""
import random

def main():
    user_score = float(input("Enter score: "))
    result = determine_result(user_score)
    print(result)
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    random_result = determine_result(random_score)
    print(random_result)

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

if __name__ == "__main__":
    main()
