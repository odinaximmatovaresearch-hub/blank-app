import streamlit as st
import streamlit_authenticator as stauth

# Foydalanuvchilar (hashed parollar bo‘lishi kerak, bu faqat misol)
credentials = {
    "usernames": {
        "user1": {"name": "User One", "password": "hashed_password1"},
        "user2": {"name": "User Two", "password": "hashed_password2"},
    }
}

# Authenticator yaratish
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="my_cookie_name",
    key="my_signature_key",
    cookie_expiry_days=30
)

# 🔐 LOGIN (yangi format!)
try:
    name, auth_status, username = authenticator.login(
        fields={'Form name': 'Login'},  # yangi talab qilinadigan parametr
        location='sidebar'              # joylashuv
    )
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

# 🧭 LOGIN NATIJASI
if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Iltimos, qayta urinib ko‘ring.")
else:
    st.info("Iltimos, login qiling.")
