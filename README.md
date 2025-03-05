# Password Strength Meter

A Python application that evaluates password strength and provides feedback for improvement. Built with Streamlit for a user-friendly interface.

## Features

- Password strength evaluation based on multiple criteria
- Visual strength indicator
- Detailed feedback for password improvement
- Strong password generator
- Common password blacklist
- User-friendly Streamlit interface

## Password Strength Criteria

A strong password should:
- Be at least 8 characters long
- Contain uppercase & lowercase letters
- Include at least one digit (0-9)
- Have one special character (!@#$%^&*)

## Scoring System

- Weak (Score: 1-2) → Short, missing key elements
- Moderate (Score: 3-4) → Good but missing some security features
- Strong (Score: 5) → Meets all criteria

## Setup Instructions

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run password_strength_meter.py
   ```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Usage

1. Enter a password in the input field to check its strength
2. View the strength score and feedback
3. Use the password generator to create a strong password
4. Follow the suggestions to improve weak passwords

## Security Note

This application runs locally on your machine. No passwords are stored or transmitted to any external servers. 