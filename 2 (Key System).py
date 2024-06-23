def check_key(user_key):
    predefined_key = "TestingKeySystem"
    return user_key == predefined_key

def main():
    user_key = input("Enter the key: ")
    if check_key(user_key):
        print("Access granted! Welcome.")
    else:
        print("Invalid key. Access denied.")

if __name__ == "__main__":
    main()
