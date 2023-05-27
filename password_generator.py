import random

def generate_password(length):
    """Generates a random password of the specified length.

    Args:
        length: The length of the password to generate.

    Returns:
        A random password of the specified length.
    """
    password = ""
    for i in range(length):
        # Modify the character pool to include the desired characters for password generation
        password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]:;'\",.<>?/")

    return password

if __name__ == "__main__":
    # Prompt the user to enter the desired length of the password
    length = int(input("Enter the length of the password you want to generate: "))

    # Call the generate_password() function to generate the password
    password = generate_password(length)

    # Display the generated password to the user
    print("Your password is:", password)
