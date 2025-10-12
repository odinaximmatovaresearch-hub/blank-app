import streamlit as st
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

authenticator = get_authenticator()
name, auth_status, username = authenticator.login("Login")

if auth_status == False:
    st.error("❌ Noto‘g‘ri login yoki parol.")
elif auth_status == None:
    st.warning("🔐 Davom etish uchun tizimga kiring.")
else:
    authenticator.logout("Chiqish", "sidebar")
    st.sidebar.success(f"👋 Xush kelibsiz, {name}!")

    st.title("🧬 NeoApop-AI Platformasi")
    st.write("Bu yerda siz molekulalarni tahlil qilish, CSV fayllarni yuklash va AI yordamida bashorat qilish imkoniyatiga egasiz.")


