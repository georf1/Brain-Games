import prompt


def welcome_user():
    """Asking for a name of user"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    return name
