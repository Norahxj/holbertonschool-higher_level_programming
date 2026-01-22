def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>."""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name and last_name:
        print(f"My name is {first_name} {last_name}", end=" ")
    elif first_name:
        print(f"My name is {first_name}", end=" ")
    elif last_name:
        print(f"My name is {last_name}", end=" ")
    else:
        print("My name is", end=" ")
