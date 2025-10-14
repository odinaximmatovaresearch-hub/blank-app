import streamlit as st
import streamlit_authenticator as stauth

# 1️⃣ — Foydalanuvchi ma'lumotlari
credentials = {
    "usernames": {
        "user1": {"name": "User One", "password": "hashed_password1"},
    }
}

# 2️⃣ — Authenticator obyektini yaratish
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="my_cookie_name",
    key="my_signature_key",
    cookie_expiry_days=30
)

# 3️⃣ — Yangi login chaqiruvi (DIQQAT: fields ishlatiladi!)
try:
    name, auth_status, username = authenticator.login(
        fields={"Form name": "Login", "Username": "Username", "Password": "Password"},
        location="sidebar"
    )
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

# 4️⃣ — Login natijasini tekshirish
if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Foydalanuvchi yoki parol xato.")
else:
    st.info("Iltimos, login qiling.")
