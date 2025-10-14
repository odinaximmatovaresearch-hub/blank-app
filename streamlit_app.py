import streamlit as st
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

authenticator = get_authenticator()

# ✅ faqat bitta usulni sinaymiz (modern versiyalar uchun)
try:
    name, auth_status, username = authenticator.login("Login", location="main")
except TypeError:
    # agar versiya eski bo‘lsa — pozitsional argument orqali
    name, auth_status, username = authenticator.login("Login", "main")

if auth_status is False:
    st.error("❌ Login yoki parol noto‘g‘ri.")
elif auth_status is None:
    st.warning("🔐 Iltimos, tizimga kiring.")
else:
    authenticator.logout("Chiqish", "sidebar")
    st.sidebar.success(f"👋 Xush kelibsiz, {name}!")

    st.title("🧬 NeoApop-AI Platformasi")
    st.write("Bu yerda siz molekulalarni tahlil qilish, CSV fayllarni yuklash va AI yordamida bashorat qilish imkoniyatiga egasiz.")
