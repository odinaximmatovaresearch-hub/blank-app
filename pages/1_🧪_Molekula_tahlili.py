import streamlit as st
import streamlit.components.v1 as components

st.title("🧬 Molekula tahlili (SMILES orqali)")

smiles = st.text_input("SMILES kiriting:")

if smiles:
    html_code = f"""
    <html>
    <head>
        <script src="https://unpkg.com/smiles-drawer@2.0.1/dist/smiles-drawer.min.js"></script>
    </head>
    <body>
        <div id="canvas"></div>
        <script>
            const smiles = "{smiles}";
            const drawer = new SmilesDrawer.Drawer({{
                width: 400,
                height: 300,
            }});
            
            SmilesDrawer.parse(smiles, function(tree) {{
                drawer.draw(tree, 'canvas', 'light', false);
            }}, function(err) {{
                document.getElementById('canvas').innerHTML = "Noto'g'ri SMILES!";
            }});
        </script>
    </body>
    </html>
    """

    components.html(html_code, height=350)






