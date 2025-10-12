import streamlit as st
from utils.descriptors import calc_descriptors
from models.model_loader import load_model, predict_activity
from utils.db_manager import save_result, init_db

st.header("🧠 AI faollik bashorati")

init_db()
model = load_model()
smiles = st.text_input("SMILES kiriting (masalan: CCO)")

if st.button("Bashorat qilish"):
    desc = calc_descriptors(smiles)
    if desc:
        if model:
            score = predict_activity(model, desc)
            st.metric("Taxminiy faollik", f"{score} %")
            save_result("demo_user", smiles, desc, score)
        else:
            st.warning("Model topilmadi. Demo rejimida ishlayapti.")
    else:
        st.error("Noto‘g‘ri SMILES.")
