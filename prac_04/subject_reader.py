"""
CP1404/CP5632 Practical
Data file -> lists program

def main():
    data = get_data("subject_data.txt")
    display_subject_details(data)

def get_data(filename)
    data = []
    with open(filename) as input_file
        for line in input_file
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subject_details(data)
    for subject in data
        print {subject[0]} is taught by {subject[1]} and has {subject[2]} students

main()
"""
def main():
    data = get_data("subject_data.txt")
    display_subject_details(data)

def get_data(filename):
    data = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subject_details(data):
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()
