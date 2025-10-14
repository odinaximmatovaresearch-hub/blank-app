import streamlit as st
import streamlit_authenticator as stauth

# Misol uchun credentials
credentials = {
    "usernames": {
        "user1": {
            "name": "User One",
            "password": "hashed_password1"  # Haqiqiy foydalanishda hashed bo'lishi kerak!
        },
        "user2": {
            "name": "User Two",
            "password": "hashed_password2"
        },
    }
}

# Authenticator yaratish
authenticator = stauth.Authenticate(
    credentials,
    "my_cookie_name",      # cookie nomi
    "my_signature_key",    # imzo kaliti
    cookie_expiry_days=30
)

# 🔒 LOGIN
try:
    # E’tibor bering: location= emas, faqat pozitsion argument
    name, auth_status, username = authenticator.login("Login", "sidebar")
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

# 🧭 LOGIN NATIJASINI TEKSHIRISH
if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Iltimos, qayta urinib ko‘ring.")
else:
    st.info("Iltimos, login qiling.")
