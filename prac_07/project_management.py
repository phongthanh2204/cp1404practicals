from project import Project
import datetime


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write('Name\tStart Date\tPriority\tCost Estimate\tCompletion\n')
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    print("Projects:")
    for project in projects:
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    selected_project = projects[choice]

    new_percentage = input("New Percentage: ")
    if new_percentage:
        selected_project.completion = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority:
        selected_project.priority = int(new_priority)


def main():
    filename = 'projects.txt'
    projects = load_projects(filename)

    # Add Menu Loop Here

    menu = "L)oad projects\nS)ave projects\nD)isplay projects\nF)ilter projects by date\nA)dd new project\nU)pdate project\nQ)uit"
    while True:
        print(menu)
        choice = input(">>> ").upper()
        if choice == 'L':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 'S':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_date = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.datetime.strptime(filter_date, '%d/%m/%Y').date()
            filtered_projects = [p for p in projects if p.start_date > filter_date]
            display_projects(filtered_projects)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            break

    save_projects(filename, projects)


if __name__ == '__main__':
    main()
