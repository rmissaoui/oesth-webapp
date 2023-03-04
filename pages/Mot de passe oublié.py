import streamlit as st
import smtplib
import random
import string
import os

st.markdown("<h1 style='text-align: center;'>Réinitialiser son mot de passe</h1>", unsafe_allow_html=True)

email = st.text_input("Email")

if st.button("Continuer"):

    # A placer à la fin de la section "if user"
    st.success("Un email contenant votre nouveau mot de passe vous a été envoyé")

    cur.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cur.fetchone()

    if user:
        sender_email = "<sender_email>"
        # sender_password = "<sender_email_password>"
        # to increase safety ?
        sender_password = os.environ.get("EMAIL_PASSWORD")
        receiver_email = email

        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        cur.execute("UPDATE users SET password=? WHERE email=?", (hash_password(new_password), email))
        conn.commit()

        smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
        smtpObj.ehlo()
        message = f"Subject: New password\n\nYour new password is: {new_password}"
        smtpObj.starttls()
        smtpObj.login(sender_email, sender_password)
        smtpObj.sendmail(sender_email, receiver_email, message)
        smtpObj.quit()

        st.success("A new password has been sent to your email.")
    else:
        st.error("Email not found.")