import streamlit as st
import sqlite3
import hashlib
from PIL import Image
import pandas as pd

from forms.dgs import dgs
from forms.eth import eth
from forms.ot import ot

if "connected" not in st.session_state :
    st.session_state["connected"] = False

# Connect to database
conn = sqlite3.connect("users.db")
cur = conn.cursor()

# Create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
conn.commit()

# Hash function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
 

# Main page
def main():
    
    page_title = "Observatoire de l’économie des stations thermales (OESTh) Formulaire 2023"
    layout = "wide"
    st.set_page_config(page_title=page_title, layout=layout)

    col1, col2, col3 = st.columns([4,6,4])



    with col2:
        image = Image.open('./images/common/logos.png')
        st.image(image, width=500)

   
    
    st.markdown("<h1 style='text-align: center;'>Observatoire de l’économie des stations thermales (OESTh) Formulaire 2023</h1>", unsafe_allow_html=True)
    
    placeholder = st.empty()
    with placeholder.container():
        # Login section
        c1, c2, c3 = st.columns((2,8,2))
        with c2:
            email = st.text_input("Email")
            password = st.text_input("Mot de passe", type='password')

            if st.button("Se connecter"):
                cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hash_password(password)))
                user = cur.fetchone()
                ### Afficher el type dans le titre formulaire
                if user:
                    st.success("Connexion réussie.")
                    ### ASK THE DB TO RETRIEVE THE ENTITY TYPE THANKS TO THE MAIL ATTRIBUTE
                    entity_type = "DGS"

                    st.session_state["connected"] = entity_type
                    st.session_state["Mail"] = email
                    st.session_state["Entity_type"] = entity_type
                    
                else:
                    st.error("Email ou mot de passe incorrect.")
           
        # New account ?
        c1, c2, c3, c4, c5, c6 = st.columns(6)
        with c2:
            st.markdown("<h8 style='text-align: center; font-size:12px;'>[Créer un compte](Créer_un_compte)</h8>", unsafe_allow_html=True)

        # Forgot password ?
        with c5:
            st.markdown("<h8 style='text-align: center; font-size:12px;'>[Mot de passe oublié](Mot_de_passe_oublié)</h8>", unsafe_allow_html=True)
        
    if st.session_state["connected"]=="DGS" :
        dgs(placeholder)
    elif st.session_state["connected"]=="ETh":
        eth(placeholder)
    elif st.session_state["connected"]=="OT":
        ot(placeholder)
    else:
        pass

if __name__ == '__main__':
    main()