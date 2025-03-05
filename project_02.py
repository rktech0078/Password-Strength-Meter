import streamlit as st
import re
import random
import string
from datetime import datetime

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="wide")

COMMON_PASSWORDS = {"password123", "12345678", "qwerty123", "admin123"}

STYLE = """
<style>
.stButton>button {width: 100%; border-radius: 5px; height: 3em; margin-top: 1em;}
.password-box, .feedback-box {background-color: #f0f2f6; padding: 1rem; border-radius: 5px; margin: 1rem 0;}
.score-box {text-align: center; padding: 1rem; border-radius: 5px; margin: 1rem 0;}
</style>
"""
st.markdown(STYLE, unsafe_allow_html=True)

def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[!@#$%^&*]", password))
    }
    
    score = sum(criteria.values())
    feedback = [
        "Use at least 8 characters" if not criteria["length"] else "",
        "Include uppercase letters" if not criteria["uppercase"] else "",
        "Include lowercase letters" if not criteria["lowercase"] else "",
        "Use numbers" if not criteria["digit"] else "",
        "Add special characters (!@#$%^&*)" if not criteria["special"] else ""
    ]
    
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["Avoid common passwords"]
    
    return score, list(filter(None, feedback))

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.sample(chars, 12))

def get_strength_label(score):
    return ["Weak", "Moderate", "Strong"][min(score // 2, 2)]

def password_checker():
    st.title("🔑 Password Strength Checker")
    password = st.text_input("Enter password:", type="password")
    if password:
        score, feedback = check_password_strength(password)
        st.markdown(f"<div class='score-box' style='border: 2px solid {['#ff4b4b','#ffa726','#66bb6a'][score//2]}'>"
                    f"<h3>{get_strength_label(score)} Password ({score}/5)</h3></div>", unsafe_allow_html=True)
        st.progress(score / 5)
        if feedback:
            st.error("\n".join(feedback))
        else:
            st.success("Your password is strong!")

def password_generator():
    st.title("🔑 Password Generator")
    if st.button("Generate Secure Password"):
        st.code(generate_strong_password(), language='plaintext')

def main():
    st.sidebar.title("🔒 Password Tools")
    option = st.sidebar.radio("Choose:", ["Password Checker", "Password Generator"])
    if option == "Password Checker":
        password_checker()
    else:
        password_generator()
    st.sidebar.markdown(f"Last updated: {datetime.now().strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
