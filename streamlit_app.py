import streamlit as st
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

authenticator = get_authenticator()

# 🟢 LOGIN – bu joy versiyaga qarab avtomatik ishlaydi
try:
    name, auth_status, username = authenticator.login("Login", "main")  # 1-usul (yangi versiya)
except TypeError:
    name, auth_status, username = authenticator.login("Login")  # 2-usul (eski versiya)

# 🔐 Auth holatini tekshirish
if auth_status == False:
    st.error("❌ Login yoki parol noto‘g‘ri.")
elif auth_status == None:
    st.warning("🔐 Tizimga kiring.")
else:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.success(f"👋 Xush kelibsiz, {name}!")

    st.title("🧬 NeoApop-AI Platformasi")
    st.write("Bu yerda siz molekulalarni tahlil qilish, CSV fayllarni yuklash va AI yordamida bashorat qilish imkoniyatiga egasiz.")
