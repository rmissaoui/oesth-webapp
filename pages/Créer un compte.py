import streamlit as st
import sqlite3
import hashlib

st.markdown("<h1 style='text-align: center;'>Créer un compte</h1>", unsafe_allow_html=True)

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


email = st.text_input("Email")
password = st.text_input("Mot de passe", type='password')
password2 = st.text_input("Confirmez le mot de passe", type='password')

st.selectbox(
'Vous êtes : ',
    ["Un DGS", "Une office de tourisme", "Un établissement thermal"])
st.text_input("Nom de votre établissement")

if password != password2:
    st.error("Les deux mots de passe entrés sont différents.")
elif st.button("Créer un compte"):
    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    if user:
        st.error("Cet email est déjà utilisé.")
    else:
        cur.execute("INSERT INTO users (email, password) VALUES (?,?)", (email, hash_password(password)))
        conn.commit()
        st.success("Votre compte a bien été créé.")