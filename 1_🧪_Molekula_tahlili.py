import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
from utils.descriptors import calc_descriptors
import pandas as pd

st.header("🧪 Molekula tahlili (SMILES orqali)")

smiles = st.text_input("SMILES kiriting (masalan: CC(=O)O yoki c1ccccc1):")

if st.button("Tahlil qilish"):
    props = calc_descriptors(smiles)
    if props:
        st.table(pd.DataFrame([props], index=[smiles]))
        mol = Chem.MolFromSmiles(smiles)
        img = Draw.MolToImage(mol, size=(300, 250))
        st.image(img, caption="2D strukturasi")
    else:
        st.error("Noto‘g‘ri SMILES format.")
