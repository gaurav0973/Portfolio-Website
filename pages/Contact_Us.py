import streamlit as st
from send_emails import send_email

st.header("Contact Me")

with st.form(key = "email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message for me")
    message = f"""\
Subject : New email from {user_email}

From : {user_email}
{raw_message}
    """
    button = st.form_submit_button("Sumbit")
    if button: #--> button is pressed then true
        send_email(message)
        st.info("Your email was sent successfully")