import streamlit as st
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", layout="wide", page_icon="🧬")

authenticator = get_authenticator()
name, auth_status, username = authenticator.login("main")

if auth_status:
    st.sidebar.success(f"Xush kelibsiz, {name}!")
    authenticator.logout("Chiqish", "sidebar")
    st.sidebar.header("🔗 Navigatsiya")
    st.sidebar.page_link("pages/1_🧪_Molekula_tahlili.py", label="🧪 Molekula tahlili")
    st.sidebar.page_link("pages/2_📁_CSV_yuklash.py", label="📁 CSV yuklash")
    st.sidebar.page_link("pages/3_🧠_AI_bashorati.py", label="🧠 AI bashorati")

elif auth_status is False:
    st.error("Login yoki parol noto‘g‘ri ❌")
else:
    st.warning("Iltimos login va parolni kiriting.")



