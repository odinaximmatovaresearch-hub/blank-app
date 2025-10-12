import streamlit as st
from models.model_loader import load_model, predict_activity

st.title("🧠 AI bashorati")

model = load_model()
value = st.slider("Qiymatni tanlang (0 yoki 1):", 0, 1)

if st.button("Bashorat qilish"):
    natija = predict_activity(model, value)
    st.success(f"🔮 Model bashorati: **{natija}**")
