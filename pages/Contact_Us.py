import streamlit as st
from sendemail import  send_email
st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    message = st.text_area("Your messages")
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_email(message)




