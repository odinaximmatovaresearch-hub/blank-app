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

# Safe login funksiyasi
def safe_login(authenticator):
    try:
        # location nomli argument emas, ikkinchi argument sifatida beriladi
        return authenticator.login("Login", "sidebar")  
    except Exception as e:
        st.error(f"Login xatoligi: {e}")
        return None, None, None

# Login chaqirish
name, auth_status, username = safe_login(authenticator)

if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Iltimos, qayta urinib ko‘ring.")
else:
    st.info("Iltimos, login qiling.")
