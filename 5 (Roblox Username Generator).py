import string
import random
import time
import os

def generate_username(length):
    """
    Generate a random username of given length.
    
    Parameters:
    length (int): The desired length of the username.
    
    Returns:
    str: A random username.
    """
    # Define the characters that can be used in the username
    chars = string.ascii_lowercase + string.digits
    
    # Make sure the first character is not a zero to avoid "0abc" usernames
    if length > 1:
        chars = chars[1:]
    
    # Generate the username
    username = ''.join(random.choice(chars) for _ in range(length))
    
    return username

def check_username(username):
    """
    Check if the username is valid and unique.
    
    Parameters:
    username (str): The username to be checked.
    
    Returns:
    bool: True if the username is valid, False otherwise.
    """
    # Check if the username contains any special characters
    if not all(c.isalnum() or c in "!@#$% " for c in username):
        return False
    
    # Check if the username is already taken
    if os.popen(f"roblox username {username}").read():
        return False
    
    return True

def main():
    print("\n\n" + "*" * 40)
    print(" Roblox Username Generator")
    print("*" * 40 + "\n")

    print("Available characters for the username:")
    print(string.ascii_lowercase)
    print(string.digits)
    print(" !", "@", "#", "$", "%")

    # Clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("1. Generate Basic Username")
        print("2. Check Username Uniqueness [BROKEN]")
        print("3. Generate Multiple Usernames")
        print("4. Exit")

        option = input("\nEnter your choice: ")

        if option == "1":
            length = int(input("\n\nEnter the desired length of your username (at least 3): "))
            if length < 3:
                print("\nUsername length should be at least 3.\n")
                continue
            username = generate_username(length)
            print(f"\nGenerated Username : {username}\n")
        elif option == "2":
            print("Enter the username you want to check for uniqueness.")
            username = input()
            if check_username(username):
                print("\nUsername generated successfully!")
            else:
                print("\nUsername already exists or is invalid.\n")
        elif option == "3":
            num_usernames = int(input("\nEnter the number of usernames you want to generate: "))
            for i in range(num_usernames):
                length = int(input(f"\nEnter the desired length for username {i+1} (at least 3): "))
                if length < 3:
                    print("\nUsername length should be at least 3.\n")
                    continue
                username = generate_username(length)
                print(f"\nGenerated Username : {username}\n")
        elif option == "4":
            break
        else:
            print("\nInvalid option. Please choose again.\n")

if __name__ == "__main__":
    main()
