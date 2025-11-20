import streamlit as st
import streamlit_authenticator as stauth

# 1️⃣ — PAROLLARNI HAQIQIY HASH QILISH
hashed_pw = stauth.Hasher(["password1", "password2"]).generate()

# 2️⃣ — Foydalanuvchi ma'lumotlari
credentials = {
    "usernames": {
        "user1": {
            "name": "User One",
            "password": hashed_pw[0]   # <-- haqiqiy hash
        },
        "user2": {
            "name": "User Two",
            "password": hashed_pw[1]
        }
    }
}

# 3️⃣ — Authenticator obyektini yaratish
authenticator = stauth.Authenticate(
    credentials,
    "my_cookie_name",
    "my_signature_key",
    cookie_expiry_days=30
)

# 4️⃣ — YANGI LOGIN USULI (fields va location bilan)
try:
    name, auth_status, username = authenticator.login(
        fields={
            "Form name": "Login",      # <-- Yangi talab
            "Username": "Username",
            "Password": "Password"
        },
        location="sidebar"             # <-- faqat "main" yoki "sidebar"
    )
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

# 5️⃣ — Natija
if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Iltimos, qayta urinib ko‘ring.")
else:
    st.info("Iltimos, login qiling.")
