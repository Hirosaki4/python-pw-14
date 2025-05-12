import json

FILE_NAME = "clients_db.json"

def load_db():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_db(db):
    with open(FILE_NAME, "w") as f:
        json.dump(db, f, indent=4)

def add_client(client):
    db = load_db()
    db.append(client)
    save_db(db)

def search_client(name):
    db = load_db()
    return [c for c in db if c["name"] == name]

def update_client(name, new_data):
    db = load_db()
    for c in db:
        if c["name"] == name:
            c.update(new_data)
    save_db(db)

def delete_client(name):
    db = load_db()
    db = [c for c in db if c["name"] != name]
    save_db(db)

# Приклад
add_client({"name": "Іван", "email": "ivan@example.com"})
update_client("Іван", {"email": "ivan123@example.com"})
print("Знайдено:", search_client("Іван"))
delete_client("Іван")
