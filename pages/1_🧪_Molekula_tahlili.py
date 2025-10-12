import streamlit as st
import pandas as pd
import numpy as np

st.header("🧬 Molekula tahlili (SMILES orqali)")

smiles = st.text_input("SMILES kiriting (masalan: CC(=O)O yoki c1ccccc1):")

if st.button("Tahlil qilish"):
    if not smiles:
        st.warning("Iltimos SMILES kiriting.")
    else:
        # RDKit o‘rniga random qiymatlar bilan demo hisoblash
        np.random.seed(len(smiles))
        props = {
            "MolWt": round(np.random.uniform(120, 350), 3),
            "LogP": round(np.random.uniform(-1, 5), 3),
            "TPSA": round(np.random.uniform(20, 150), 3),
            "HBA": np.random.randint(0, 10),
            "HBD": np.random.randint(0, 5),
            "RotatableBonds": np.random.randint(0, 10)
        }
        st.table(pd.DataFrame([props], index=[smiles]))
        st.info("🧪 Bu demo versiya — RDKit ishlatmasdan taxminiy qiymatlar qaytaradi.")
