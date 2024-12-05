import pwinput
from termcolor import colored
import string

# try and accept accordingly to make a program that will not crash
# learn what the type hints are and how to use them e.g. -> str, -> bool, -> int

def get_password(prompt: str) -> str:
    """
    Get a password from the user.
    """
    user_input_password = input(prompt)
    return user_input_password


def get_username(prompt: str) -> str:
    """
    Get a username from the user.
    """
    user_input_username = input(prompt)
    return user_input_username

def validate_password(password: str) -> bool:
    """
    Validate a password.
    a valid password should contain:
    - at least 8 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character
    """
    special_characters = string.punctuation
    viable = False

    if len(password) >= 8:
        viable = True
    
    if not viable:
        for character in password:
            if character.isupper():
                viable = True
                break
    
    if not viable:
        for character in password:
            if character.islower():
                viable = True
                break
    
    if not viable:
        for character in password:
            if character.isdigit():
                viable = True
                break
    
    if not viable:
        for character in password:
            if character in special_characters:
                viable = True
                break
    
    return viable

def validate_username(username: str) -> bool:
    """
    Validate a username.
    a valid username should contain:
    - at least 3 characters
    - no alphanumeric characters
    """
def save_user_info(username: str, password: str) -> None:
    database_path = "./Database/users.csv"
    """
    Save the user's information to a file.
    hints:
    - learn how to read and write a CSV file
    - use the with statement to open a file
    - append the username and password to the file
    - ensure theres no duplicates
    """


if __name__ == "__main__":
    #use to test the functions
    pass
