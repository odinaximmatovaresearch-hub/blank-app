import streamlit as st

try:
    from rdkit import Chem
    from rdkit.Chem import Draw
    RDKit_AVAILABLE = True
except ImportError:
    RDKit_AVAILABLE = False

import py3Dmol

st.title("🧬 Molekula tahlili (SMILES orqali)")

smiles = st.text_input("SMILES kiriting (masalan: CC(=O)O yoki c1ccccc1):")

def draw_3d(smiles):
    view = py3Dmol.view(width=400, height=400)
    view.addModel(smiles, "smi")
    view.setStyle({"stick": {}})
    view.zoomTo()
    view.show()
    return view

if smiles:
    if RDKit_AVAILABLE:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            st.image(Draw.MolToImage(mol), caption="2D tasvir (RDKit)")
        else:
            st.error("❌ Noto‘g‘ri SMILES kiritildi.")
    else:
        st.warning("⚠ RDKit yo‘q — 3D ko‘rinish chizilmoqda.")
        view = draw_3d(smiles)
        st.components.v1.html(view._repr_html_(), height=450)





