import streamlit as st
import pandas as pd
from utils.descriptors import calc_descriptors

st.header("📁 CSV yuklash (batch tahlil)")
st.write("Faylda `smiles` nomli ustun bo‘lishi kerak.")

file = st.file_uploader("CSV faylni tanlang", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())
    if "smiles" not in df.columns:
        st.error("CSV faylda `smiles` ustuni topilmadi.")
    elif st.button("Hisoblashni boshlash"):
        results = []
        for smi in df["smiles"]:
            desc = calc_descriptors(smi)
            if desc:
                desc["SMILES"] = smi
                results.append(desc)
        res_df = pd.DataFrame(results)
        st.success(f"{len(res_df)} ta molekula tahlil qilindi ✅")
        st.dataframe(res_df.head())
        csv = res_df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Natijani yuklash", csv, "results.csv")
