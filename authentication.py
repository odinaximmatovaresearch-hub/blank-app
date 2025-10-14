import streamlit as st
import streamlit_authenticator as stauth
import inspect
import traceback

# Misol credentials (siz o'zingiznikini qo'ying)
credentials = {
    "usernames": {
        "user1": {"name": "User One", "password": "hashed_password1"},
    }
}

authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="my_cookie_name",
    key="my_signature_key",
    cookie_expiry_days=30
)

def smart_login(authenticator, label="Login", location="sidebar"):
    """
    Avtomatik ravishda streamlit_authenticator.login() ni chaqiradi
    - Har xil versiyalar uchun bir nechta chaqirish usullarini sinaydi.
    - Imzo (signature) ni sahifada ko'rsatadi va xatolarni aniq chiqaradi.
    """
    try:
        # Bound method imzosini oling
        sig = inspect.signature(authenticator.login)
        params = list(sig.parameters.keys())
        st.write("`authenticator.login` imzosi:", str(sig))
    except Exception as e:
        st.write("Imzoni olishda xato:", e)
        params = []

    # 1) Yangi (v0.4+) — fields parametri mavjud bo'lsa
    if "fields" in params:
        st.write("Urinish: v0.4+ (fields=...) chaqiradi")
        try:
            return authenticator.login(fields={"Form name": label}, location=location)
        except Exception as e:
            st.write("v0.4+ chaqirish xatosi:")
            st.write(traceback.format_exc())

    # 2) v0.3.x — ikkita pozitsion argument ("label", "sidebar")
    # (ba'zan parametrlarda 'location' bo'lishi mumkin, shuning uchun first try pozitsion)
    try:
        st.write("Urinish: v0.3.x (positionals) chaqiradi")
        return authenticator.login(label, location)
    except TypeError as e:
        # TypeError ko'pincha "multiple values for argument 'location'" yoki mismatched signature
        st.write("v0.3.x pozitsion chaqirish TypeError:")
        st.write(traceback.format_exc())
    except Exception as e:
        st.write("v0.3.x pozitsion chaqirish boshqa xato:")
        st.write(traceback.format_exc())

    # 3) v0.2.x yoki eski — faqat bitta argument (form_name) yoki keyword location
    try:
        st.write("Urinish: eski (label only yoki location=...) chaqiradi")
        # avvalo label bilan
        return authenticator.login(label)
    except TypeError:
        # keywork bilan urinib ko'ramiz
        try:
            return authenticator.login(label, location=location)
        except Exception:
            st.write("Eski versiya uchun ham chaqirish xatosi:")
            st.write(traceback.format_exc())
    except Exception:
        st.write("Eski versiya uchun chaqirishda boshqa xato:")
        st.write(traceback.format_exc())

    # Agar barcha urinishlar muvaffaqiyatsiz bo'lsa:
    st.error("Barcha chaqirish usullari sinab ko'rildi — login chaqirilolmadi. Quyidagi xatolar sahifada ko'rsatilgan.")
    return None, None, None

# Foydalanish
name, auth_status, username = smart_login(authenticator)

if auth_status:
    st.success(f"Salom, {name}!")
elif auth_status is False:
    st.error("Login muvaffaqiyatsiz. Iltimos, qayta urinib ko'ring.")
else:
    st.info("Iltimos, login qiling.")
