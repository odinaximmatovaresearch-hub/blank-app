import streamlit as st
import streamlit_authenticator as stauth

# 1️⃣ — Foydalanuvchi parolini oldindan hash qiling:
hashed_passwords = stauth.Hasher(["123456"]).generate()

# 2️⃣ — Foydalanuvchi ma'lumotlari
credentials = {
    "usernames": {
        "user1": {
            "name": "User One",
            "password": hashed_passwords[0],  # <-- HASHED PAROL
        },
    }
}

# 3️⃣ — Authenticator obyektini yaratish
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="my_cookie_name",
    key="my_signature_key",
    cookie_expiry_days=30
)

# 4️⃣ — Login oynasi (yangilangan 'fields')
try:
    name, auth_status, username = authenticator.login(
        fields={
            "Form name": "Login",
            "Username": "Foydalanuvchi nomi",
            "Password": "Parol"
        },
        location="sidebar"
    )
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

# 5️⃣ — Login natijasi
if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("❌ Login yoki parol noto‘g‘ri.")
else:
    st.info("Iltimos, login qiling.")
