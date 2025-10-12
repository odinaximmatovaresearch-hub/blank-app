import streamlit as st
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

authenticator = get_authenticator()

# 💡 LOGIN funksiyasi uchun universal usul
try:
    # yangi versiyalar uchun
    name, auth_status, username = authenticator.login("Login", location="main")
except TypeError:
    try:
        # eski versiyalar uchun
        name, auth_status, username = authenticator.login("Login", "main")
    except Exception:
        # eng eski versiya – umuman parametrlarsiz
        name, auth_status, username = authenticator.login("Login")

# 🔐 Auth holatini tekshiramiz
if auth_status == False:
    st.error("❌ Login yoki parol noto‘g‘ri.")
elif auth_status == None:
    st.warning("🔐 Tizimga kiring.")
else:
    authenticator.logout("Chiqish", "sidebar")
    st.sidebar.success(f"👋 Xush kelibsiz, {name}!")

    st.title("🧬 NeoApop-AI Platformasi")
    st.write("Bu yerda siz molekulalarni tahlil qilish, CSV fayllarni yuklash va AI yordamida bashorat qilish imkoniyatiga egasiz.")
