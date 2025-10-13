# streamlit_app.py
import streamlit as st
import inspect
from utils.authentication import get_authenticator

st.set_page_config(page_title="NeoApop-AI", page_icon="🧬", layout="wide")

authenticator = get_authenticator()

def safe_login(auth):
    """
    authenticator.login ni turli versiyalarga moslab chaqiradi.
    - agar keyword 'location' qabul qilsa: location='main'
    - agar ikkinchi pozitsional argumentni qabul qilsa: 'main'
    - aks holda parametrlarsiz chaqiradi
    """
    login_fn = auth.login
    sig = None
    try:
        sig = inspect.signature(login_fn)
        params = sig.parameters
    except Exception:
        params = {}

    # 1) agar 'location' keyword qabul qilsa
    if "location" in params:
        try:
            return login_fn("Login", location="main")
        except Exception:
            pass

    # 2) agar ikkinchi pozitsional argument mavjud bo'lsa
    # (masalan: login(form_name, location) )
    try:
        # sinab ko'rish: pozitsional usul
        return login_fn("Login", "main")
    except Exception:
        pass

    # 3) fallback — parametrlarsiz chaqirish
    try:
        return login_fn("Login")
    except Exception as e:
        # agar hammasi xato bersa, xatoni ko'rsatamiz caller ga
        raise e

# Endi xavfsiz chaqiramiz
try:
    name, auth_status, username = safe_login(authenticator)
except Exception as e:
    # Agar login bilan bog'liq kritik xato bo'lsa — foydalanuvchiga aniq ko'rsatish
    st.error("Autentifikatsiya ishga tushmadi — Manage app → Logs ni tekshiring.")
    # hamda logs uchun xatoni konsolga chiqarish (loglarda ko'rinsin)
    raise

# Auth statusni tekshirish va UI
if auth_status is False:
    st.error("❌ Login yoki parol noto‘g‘ri.")
elif auth_status is None:
    st.warning("🔐 Iltimos, tizimga kiring.")
else:
    try:
        authenticator.logout("Chiqish", "sidebar")
    except Exception:
        # turli versiya uchun ham xatolik bo'lmasligi uchun fallback
        try:
            authenticator.logout()
        except Exception:
            pass

    st.sidebar.success(f"👋 Xush kelibsiz, {name}!")
    st.title("🧬 NeoApop-AI Platformasi")
    st.write("Sahifalardan birini tanlang.")
