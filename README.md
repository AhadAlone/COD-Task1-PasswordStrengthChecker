# PasswordStrengthChecker
Python Tool for Password Strength Checking, Ready to setup and use
Task 1
Name : Shaik Abdul Ahad
ID : CT08DS1276
Domain: Cyber Security and Ethical Hacking
Mentor: Sravani Gouni
Description:
## Password Strength Checker

This repository contains a Python script designed to evaluate the strength of a given password based on various criteria. The script not only checks for the presence of digits, uppercase and lowercase letters, and special characters, but it also calculates the entropy of the password to provide a comprehensive assessment of its strength. 

### Features

1. **Password Length Check**:
   - Ensures the password is at least 8 characters long.

2. **Character Variety Check**:
   - Checks for the inclusion of at least one digit.
   - Verifies the presence of at least one uppercase letter.
   - Ensures there is at least one lowercase letter.
   - Confirms the presence of at least one special character from the set `!@#$%^&*()_+=-{};:'<>,./?`.

3. **Entropy Calculation**:
   - Calculates the Shannon entropy of the password to gauge its unpredictability.
   - Provides feedback if the entropy is below a threshold of 30.

4. **Strength Assessment**:
   - Combines the results of the checks and entropy calculation to determine an overall password strength.
   - Maps the strength score to a descriptive message: Very Weak, Weak, Medium, Strong, Very Strong, Very Very Strong.

5. **Entropy to Strength Percentage Conversion**:
   - Converts the calculated entropy into a strength percentage for a more nuanced evaluation.

6. **User Interaction**:
   - Prompts the user to input a password.
   - Displays the password strength and any errors or suggestions for improvement.

### Usage

1. **Clone the Repository**:
   ```sh
   git clone "https://github.com/AhadAlone/PasswordStrengthChecker.git"
   cd password-strength-checker
   ```

2. **Run the Script**:
   ```sh
   python password_strength_checker.py
   ```

3. **Enter a Password**:
   - Input the password when prompted to receive an evaluation of its strength and suggestions for improvement.

### Example

```sh
$ python password_strength_checker.py
Enter Password: Passw0rd!

Password strength: Strong

Strength: 45.67%
```

### Functions

- **password_strength(password)**: Evaluates the password based on length, digit inclusion, case variety, and special character presence. Returns a strength score and a list of error messages.
- **calculate_entropy(password)**: Computes the Shannon entropy of the password.
- **entropy_to_strength_percentage(entropy)**: Converts entropy value into a percentage representing password strength.
- **get_password_strength_message(strength)**: Maps the numerical strength score to a descriptive strength message.


### Contributions

Contributions are welcome! Please fork this repository and submit pull requests for any enhancements or bug fixes.

### Contact

For any issues or feature requests, please create an issue in this repository.
