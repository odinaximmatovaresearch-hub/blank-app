import streamlit as st
import streamlit_authenticator as stauth

# 🔐 Misol uchun foydalanuvchi ma'lumotlari
credentials = {
    "usernames": {
        "user1": {"name": "User One", "password": "hashed_password1"},
    }
}

# 🔒 Authenticator obyektini yaratish
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="my_cookie_name",
    key="my_signature_key",
    cookie_expiry_days=30
)

# ✅ Yangi login usuli (0.4.x va undan yuqori uchun)
try:
    name, auth_status, username = authenticator.login(
        fields={"Form name": "Login"},  # Yangi format!
        location="sidebar"
    )
except Exception as e:
    st.error(f"Login xatoligi: {e}")
    name, auth_status, username = None, None, None

# 🔁 Natijani tekshirish
if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Parol yoki foydalanuvchi noto‘g‘ri.")
else:
    st.info("Iltimos, login qiling.")
