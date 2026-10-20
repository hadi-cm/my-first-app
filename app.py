import streamlit as st

st.set_page_config(page_title="Faz Fidar Parsian")

st.title("Faz Fidar Parsian")
st.subheader("Engineering and Technology Services")

st.divider()

st.write("Welcome to Faz Fidar Parsian company.")
st.write("We provide professional engineering services.")

st.divider()

st.header("Contact Us")
name = st.text_input("Your Name")
phone = st.text_input("Phone Number")

if st.button("Send Request"):
    if name and phone:
        st.success("Thank you! We will contact you soon.")
    else:
        st.error("Please enter your name and phone number.")

st.divider()

st.info("Faz Fidar Parsian | Contact us for more information")
