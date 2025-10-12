import streamlit as st
from utils.authentication import get_authenticator
from utils.language import LANGS, t

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

lang_name = st.sidebar.selectbox("🌍 Tilni tanlang:", list(LANGS.keys()))
lang_code = LANGS[lang_name]

authenticator = get_authenticator()
name, auth_status, username = authenticator.login("Login", location="main")

if auth_status:
    authenticator.logout(t("Chiqish", lang_code), "sidebar")
    st.sidebar.success(f"{t('Xush kelibsiz', lang_code)}, {name}!")
    st.title(t("NeoApop-AI — Dori kashfiyoti platformasi", lang_code))
    st.write(t("Pastdagi sahifalardan birini tanlang.", lang_code))
elif auth_status is False:
    st.error(t("Login yoki parol noto‘g‘ri ❌", lang_code))
else:
    st.warning(t("Iltimos login va parolni kiriting.", lang_code))

