# Random-Password
# Random Password Generator with GUI
This project is a Random Password Generator built using Python and the tkinter library for the graphical user interface (GUI). The application allows users to generate secure passwords of customizable length, ensuring at least one lowercase letter, one uppercase letter, one digit, and one special character.

## Features
- Customizable Password Length: Input the desired length of the password.
- Secure Passwords: Ensures passwords meet basic security standards (lowercase, uppercase, digit, and special character).
- Easy to Use: User-friendly interface to generate and view passwords.
- Error Handling: Displays error messages for invalid inputs (e.g., non-integer values or lengths below 4).
## How to Use
#### 1. Launch the Application:
- Run the script using Python (python script_name.py).
#### 2. Input Password Length:
- Enter the desired password length in the input box. (Minimum: 4 characters.)
#### 3. Generate Password:
- Click the "Generate Password" button to create a random password.
#### 4. View the Password:
- The generated password will appear in the "Generated Password" text box.
#### 5. Error Messages:
- If the input is invalid, a pop-up message will notify you.
## Installation
####  Prerequisites
  - Python 3.x installed on your system.
####  Steps
   - Clone or download the script.
   - Run the following command to execute the application:
```
python script_name.py
```
   Replace script_name.py with the name of the script file.
### Code Structure
- generate_password(length):
  - Generates a secure random password of the specified length.
- on_generate_click():
  - Handles the button click event to validate input and display the password.
- GUI Layout:
  - Includes input boxes for password length and output, as well as a "Generate Password" button.
### Dependencies
The project only relies on the following libraries:

  - random (Standard Library)
  - string (Standard Library)
  - tkinter (Standard Library for GUI)
No additional installations are required.

## Example Screenshot
![Random](https://github.com/user-attachments/assets/a5f7986f-670d-4a60-aa33-64cf19e2f2be)


Enjoy using the Random Password Generator! 😊
