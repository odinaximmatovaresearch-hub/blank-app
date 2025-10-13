# utils/authentication.py
import streamlit_authenticator as stauth

def get_authenticator():
    credentials = {
        "usernames": {
            "admin": {"name": "Admin", "password": "demo123"},
            "odina": {"name": "Odina", "password": "odina456"},
            "guest": {"name": "Guest", "password": "guest789"},
        }
    }

    # Har qanday streamlit-authenticator versiyasiga mos qurish
    try:
        # yangi API (keyword argumentlar bilan)
        authenticator = stauth.Authenticate(
            credentials=credentials,
            cookie_name="neoapop_cookie",
            key="neoapop_key",
            cookie_expiry_days=1
        )
    except Exception:
        # eski API (pozitsional argumentlar bilan)
        authenticator = stauth.Authenticate(
            credentials,
            "neoapop_cookie",
            "neoapop_key",
            cookie_expiry_days=1
        )

    return authenticator
