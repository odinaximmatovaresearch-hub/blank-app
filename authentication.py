import streamlit as st
import streamlit_authenticator as stauth

# Parolni hash qilish
hashed_pw = stauth.Hasher(["123456"]).generate()

credentials = {
    "usernames": {
        "user1": {
            "name": "User One",
            "password": hashed_pw[0]
        }
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "mycookie",
    "mykey",
    cookie_expiry_days=30
)

try:
    name, auth_status, username = authenticator.login(
        fields={
            "Form name": "Login",
            "Username": "Username",
            "Password": "Password"
        },
        location="main"
    )
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("❌ Login yoki parol xato.")
else:
    st.info("Iltimos, login qiling.")
