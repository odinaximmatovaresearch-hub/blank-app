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
        # 'location' parametrini to'g'ri beramiz
        return authenticator.login("Login", location="sidebar")  # yoki 'main', 'unrendered'
    except Exception as e:
        st.error(f"Login xatoligi: {e}")
        return None, None, None

# Login chaqirish
name, auth_status, username = safe_login(authenticator)

if auth_status:
    st.write(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz")
else:
    st.info("Iltimos, login qiling")
