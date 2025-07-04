import json


def load_users():
    with open("users.json", "r") as file:
        return json.load(file)


USERS = load_users()


def filter_users_by_name(name):
    """Filter users by their name (case-insensitive) and print the matches."""
    filtered_users = [
        user for user in USERS if user["name"].lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    """Filter users by their exact age and print the matches."""
    filtered_by_age = [
        user for user in USERS if user.get("age") == age
    ]

    for user in filtered_by_age:
        print(user)


def filter_by_email(email):
    """Filter users by their email address (case-insensitive) and print the matches."""
    filtered_by_mail = [
        user for user in USERS if user["email"].lower() == email.lower()
    ]

    for user in filtered_by_mail:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? "
        "(Currently, only 'name', 'age' or 'email' is supported): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        try:
            age_to_search = input("Enter an age to filter users: ").strip()
            filter_users_by_age(int(age_to_search))
        except ValueError:
            print("Enter a valid number for age")
    elif filter_option == "email":
        email = input("Enter an email to filter users: ").strip()
        filter_by_email(email)
    else:
        print("Filtering by that option is not yet supported.")
