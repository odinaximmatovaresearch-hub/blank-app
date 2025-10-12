import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw

st.title("🧬 Molekula tahlili (SMILES orqali)")
smiles = st.text_input("SMILES kiriting (masalan: CC(=O)O yoki c1ccccc1):")

if smiles:
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            st.image(Draw.MolToImage(mol), caption="Molekula tasviri")
        else:
            st.error("❌ Noto‘g‘ri SMILES kiritildi.")
    except Exception as e:
        st.error(f"Xato yuz berdi: {e}")
