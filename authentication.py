import streamlit as st
import streamlit_authenticator as stauth

# Authenticator yaratish (misol)
credentials = {
    "usernames": {
        "user1": {"name": "User One", "password": "hashed_password1"},
        "user2": {"name": "User Two", "password": "hashed_password2"},
    }
}

authenticator = stauth.Authenticate(
    credentials,
    "my_cookie_name",
    "my_signature_key",
    cookie_expiry_days=30
)

# Login to'g'ridan-to'g'ri chaqiriladi
try:
    name, auth_status, username = authenticator.login("Login", location="sidebar")
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Iltimos, qayta urinib ko‘ring.")
else:
    st.info("Iltimos, login qiling.")
