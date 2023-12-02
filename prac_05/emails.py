"""
Emails to Names
Estimate: 20 minutes
Actual: 17 minutes

def extract_name(email)
    prefix = email.split
    parts = prefix.split
    name = join(part.capitalize() for part in parts
    return name

emails_to_names = {}

get email
while email
    name = extract_name(email)
    get confirmation = Is your name {name}? (Y/n)

    if confirmation != '' and confirmation != 'y':
        name = input("Name: ").title().strip()

    emails_to_names[email] = name
    get emails

for email, name in emails_to_names.items():
    print {name} ({email})
"""
def extract_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(part.capitalize() for part in parts)
    return name

emails_to_names = {}

email = input("Email: ")
while email:
    name = extract_name(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

    if confirmation != '' and confirmation != 'y':
        name = input("Name: ").title().strip()

    emails_to_names[email] = name
    email = input("Email: ")

for email, name in emails_to_names.items():
    print(f"{name} ({email})")
