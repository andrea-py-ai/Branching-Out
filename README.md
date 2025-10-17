# 🧩 User Filter Script

A simple Python script that loads user data from a JSON file and allows filtering by **name**, **age**, or **email** through the command line.

---

## 📄 How It Works

1. The script reads user data from a file named `users.json`.  
2. You’ll be prompted to choose a filter key (`name`, `age`, or `email`).  
3. Enter a value, and the program will display all matching users.

Filtering is **case-insensitive** for text values and **exact** for numeric ones.

---

## ⚙️ Requirements

- Python 3.x  
- A valid `users.json` file in the same directory.

Example `users.json`:
```json
[
  {"name": "Alice", "age": 30, "email": "alice@example.com"},
  {"name": "Bob", "age": 25, "email": "bob@example.com"}
]
```

---

## ▶️ Usage

Run the script from the terminal:
```bash
python main.py
```

Example interaction:
```
What would you like to filter by? (name, age, email): name
Enter a value for name: Alice
{'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
```

---

## 🧠 Features

- Loads user data from a JSON file  
- Filters users by a chosen key  
- Case-insensitive search for text fields  
- Graceful handling of invalid input  

---

## 📦 File Structure
```
├── main.py
└── users.json
```

---

## 🪶 License
This project is open-source and available for educational or personal use.
