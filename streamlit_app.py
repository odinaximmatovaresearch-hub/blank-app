import streamlit as st
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

authenticator = get_authenticator()
name, auth_status, username = authenticator.login("Login", location="main")

if auth_status:
    authenticator.logout("Chiqish", "sidebar")
    st.sidebar.success(f"👋 Salom, {name}!")
    st.title("NeoApop-AI — AI asosidagi dori tahlili platformasi 💊")
    st.write("Pastdagi **Pages** menyusi orqali sahifalarga o‘ting.")
elif auth_status is False:
    st.error("Login yoki parol noto‘g‘ri ❌")
else:
    st.warning("Iltimos login va parolni kiriting.")
