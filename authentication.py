import streamlit_authenticator as stauth

def get_authenticator():
    credentials = {
        "usernames": {
            "admin": {
                "name": "Admin",
                "password": stauth.Hasher(["demo123"]).generate()[0]
            },
            "odina": {
                "name": "Odina",
                "password": stauth.Hasher(["odina456"]).generate()[0]
            },
            "guest": {
                "name": "Guest User",
                "password": stauth.Hasher(["guest789"]).generate()[0]
            }
        }
    }

    authenticator = stauth.Authenticate(
        credentials,
        cookie_name="neoapop_ai_cookie",
        key="neoapop_ai_sig",
        cookie_expiry_days=1
    )

    return authenticator

