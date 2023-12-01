
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

def get_data(filename):
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(filename) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])  # Convert the number of students to integer
            data.append(parts)
    return data

def display_subject_details(data):
    """Display subject details from the data."""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

def main():
    data = get_data("subject_data.txt")
    display_subject_details(data)

main()
