from deep_translator import GoogleTranslator

LANGS = {
    "O‘zbek": "uz",
    "English": "en",
    "Русский": "ru",
    "Français": "fr"
}

def t(text, lang):
    """Matnni 4 tilda tarjima qiladi"""
    try:
        if lang == "uz":
            return text
        return GoogleTranslator(source="auto", target=lang).translate(text)
    except:
        return text
