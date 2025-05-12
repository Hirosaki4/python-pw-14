import json

FILE_NAME = "contacts.json"

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

def load_contacts():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Додати контакт
def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)

# Приклад
add_contact("Олена", "0981234567")
add_contact("Андрій", "0639876543")
print("Контакти:", load_contacts())
