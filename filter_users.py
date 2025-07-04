import json


def load_users():
    """Load and return user data from the JSON file."""
    with open("users.json", "r") as file:
        return json.load(file)


USERS = load_users()


def filter_users(key, value):
    """Filter users by a given key and value (case-insensitive for strings)."""
    if isinstance(value, str):
        return [user for user in USERS if user.get(key, "").lower() == value.lower()]
    return [user for user in USERS if user.get(key) == value]


def print_users(users):
    """Print a list of user dictionaries."""
    if not users:
        print("No users found.")
    for user in users:
        print(user)


def main():
    filter_option = input("What would you like to filter by? (name, age, email): ").strip().lower()

    if filter_option in ["name", "age", "email"]:
        value = input(f"Enter a value for {filter_option}: ").strip()
        if filter_option == "age":
            try:
                value = int(value)
            except ValueError:
                print("Invalid age. Must be a number.")
                exit()
        filtered = filter_users(filter_option, value)
        print_users(filtered)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()