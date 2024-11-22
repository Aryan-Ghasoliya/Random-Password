import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password(length=12):
    """
    Generate a random password of specified length.

    Parameters:
        length (int): Length of the password to be generated.

    Returns:
        str: The generated password.
    """
    if length < 4:  # Minimum length requirement for a secure password
        return "Error: Password length should be at least 4 characters."

    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(string.ascii_lowercase),  # At least one lowercase letter
        random.choice(string.ascii_uppercase),  # At least one uppercase letter
        random.choice(string.digits),          # At least one digit
        random.choice(string.punctuation)      # At least one special character
    ]

    # Fill the rest of the password length with random choices from the character pool
    password += random.choices(characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)


def on_generate_click():
    """Handle the button click event to generate a password."""
    try:
        length = int(entry_length.get())
        password = generate_password(length)
        if "Error" in password:
            messagebox.showerror("Invalid Input", password)
        else:
            entry_result.delete(0, tk.END)
            entry_result.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer for password length.")


# Create the main application window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Create widgets
label_length = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
label_length.pack(pady=10)

entry_length = tk.Entry(root, font=("Arial", 12), justify="center")
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", font=("Arial", 12), command=on_generate_click)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="Generated Password:", font=("Arial", 12))
label_result.pack(pady=10)

entry_result = tk.Entry(root, font=("Arial", 12), justify="center")
entry_result.pack(pady=5)

# Run the application
root.mainloop()
