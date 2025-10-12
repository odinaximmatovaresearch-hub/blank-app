import streamlit_authenticator as stauth

def get_authenticator():
    credentials = {
        "usernames": {
            "admin": {"name": "Admin", "password": "demo123"},
            "odina": {"name": "Odina", "password": "odina456"},
            "guest": {"name": "Guest", "password": "guest789"}
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        cookie_name="neoapop_ai_cookie",
        key="neoapop_ai_sig",
        cookie_expiry_days=1
    )

    return authenticator

