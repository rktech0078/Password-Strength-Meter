import streamlit as st
import re
import random
import string
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        margin-top: 1em;
    }
    .password-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .feedback-box {
        background-color: #e6f3ff;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .score-box {
        text-align: center;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .radio-group {
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Common weak passwords to check against
COMMON_PASSWORDS = [
    "password123", "12345678", "qwerty123", "admin123",
    "letmein123", "welcome123", "monkey123", "football123"
]

def check_password_strength(password):
    """
    Check password strength and return score and feedback
    Returns: (score, feedback)
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter")
    
    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*)")
    
    # Check against common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This is a common password. Please choose a stronger one")
    
    return score, feedback

def generate_strong_password():
    """Generate a strong password that meets all criteria"""
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    
    # Generate password with at least one of each required character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest with random characters
    all_chars = lowercase + uppercase + digits + special
    while len(password) < 12:  # Generate a 12-character password
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def get_strength_color(score):
    """Return color based on password strength"""
    if score <= 2:
        return "#ff4b4b"  # Red
    elif score <= 4:
        return "#ffa726"  # Orange
    else:
        return "#66bb6a"  # Green

def show_password_checker():
    """Display the password strength checker interface"""
    st.title("Password Strength Checker")
    st.markdown("Enter your password below to check its strength and get feedback.")
    
    password = st.text_input("Enter your password:", type="password", key="password_input")
    
    if password:
        score, feedback = check_password_strength(password)
        
        # Display strength indicator with custom styling
        st.markdown(f"""
            <div class="score-box" style="background-color: {get_strength_color(score)}20; border: 2px solid {get_strength_color(score)};">
                <h3 style="color: {get_strength_color(score)};">
                    {'Weak Password' if score <= 2 else 'Moderate Password' if score <= 4 else 'Strong Password!'}
                </h3>
                <h2 style="color: {get_strength_color(score)};">{score}/5</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # Display progress bar
        st.progress(score / 5)
        
        # Display feedback in a styled box
        if feedback:
            st.markdown("""
                <div class="feedback-box">
                    <h4>Suggestions for improvement:</h4>
                    <ul>
            """, unsafe_allow_html=True)
            for item in feedback:
                st.markdown(f"<li>{item}</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)
        else:
            st.success("Your password meets all security criteria! 🎉")

def show_password_generator():
    """Display the password generator interface"""
    st.title("Password Generator")
    st.markdown("Generate a secure password that meets all security criteria.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("Generate Strong Password", key="generate_button"):
            generated_password = generate_strong_password()
            st.markdown("""
                <div class="password-box">
                    <h4>Generated Password:</h4>
                    <h6>Immediately Copy to Clipboard</h6>
                    <code style="font-size: 1.2em;">{}</code>
                </div>
            """.format(generated_password), unsafe_allow_html=True)
            
            # Add copy button
            # st.markdown(f"""
            #     <button onclick="navigator.clipboard.writeText('{generated_password}')" 
            #             style="background-color: #4CAF50; color: white; padding: 10px; border: none; border-radius: 5px; cursor: pointer;">
            #         Copy to Clipboard
            #     </button>
            # """, unsafe_allow_html=True)
            
            
            st.success("This password meets all security criteria!")
    
    with col2:
        st.markdown("### Password Requirements")
        st.markdown("""
        The generated password will include:
        - Minimum 12 characters
        - At least one uppercase letter
        - At least one lowercase letter
        - At least one number
        - At least one special character
        - Random character placement
        """)

def main():
    # Sidebar
    with st.sidebar:
        st.title("🔒 Password Strength Meter")
        st.markdown("---")
        
        # Radio buttons for navigation
        st.markdown('<div class="radio-group">', unsafe_allow_html=True)
        page = st.radio(
            "Select Tool:",
            ["Password Strength Checker", "Password Generator"],
            key="page_selector"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### About")
        st.markdown("""
        This tool helps you create strong passwords by:
        - Evaluating password strength
        - Providing detailed feedback
        - Generating secure passwords
        """)
        st.markdown("---")
        st.markdown(f"Last updated: {datetime.now().strftime('%Y-%m-%d')}")

    # Main content based on selection
    if page == "Password Strength Checker":
        show_password_checker()
    else:
        show_password_generator()

if __name__ == "__main__":
    main() 