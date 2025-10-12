import streamlit as st

try:
    from rdkit import Chem
    from rdkit.Chem import Draw
    RDKit_AVAILABLE = True
except ImportError:
    RDKit_AVAILABLE = False

st.title("🧬 Molekula tahlili (SMILES orqali)")

smiles = st.text_input("SMILES kiriting (masalan: CC(=O)O yoki c1ccccc1):")

if smiles:
    if not RDKit_AVAILABLE:
        st.error("RDKit o‘rnatilmagan — strukturani chizish imkoni yo‘q.")
    else:
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            st.image(Draw.MolToImage(mol), caption="Molekula 2D tasviri")
        else:
            st.error("❌ Noto‘g‘ri SMILES kiritildi.")


