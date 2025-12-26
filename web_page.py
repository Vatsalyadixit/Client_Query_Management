import streamlit as st
from auth import login, signup
from Client_page import client_page
from support_page import support_page
from Background_image import bg_image_1
from Background_image import bg_image_2
from Background_image import bg_image_3
from Background_image import bg_image_4


col1, col2 = st.columns([8,2]) # Setting up refresh button 

with col2:
    if st.button("🔁 Refresh"):
        st.rerun()

if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
    st.session_state.user_role = ""
    st.session_state.user_name = ""

# LOGIN / SIGNUP PAGE Setup
if not st.session_state.is_logged_in:

    theme = st.sidebar.segmented_control("Theme",["Dark","Light"]) # make a theme changer
    if theme == "Dark":
        bg_image_1()
    else:
        bg_image_3()
    
    st.title("Client Query Management System")

    menu = st.sidebar.segmented_control("Menu", ["Login", "Signup"])

    if menu == "Signup":
        st.text("Support user create please account with your official mail_id from Guvi")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.segmented_control("Who are you?", ["Client", "Support"])

        if st.button("Signup"):
            msg = signup(username, password, role.lower())
            st.success(msg)

    if menu == "Login":
        st.text("Support user please login with your official mail_id from Guvi")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        role = st.segmented_control("Who are you?", ["Client", "Support"])

        if st.button("Login"):
            user_role, msg = login(username, password, role.lower())

            if user_role:
                st.session_state.is_logged_in = True
                st.session_state.user_role = user_role
                st.session_state.user_name = username
                st.rerun()
            else:
                st.error(msg)

# Web_page setup
else:

    if st.session_state.user_role == "client":
        client_page(st.session_state.user_name)

    elif st.session_state.user_role == "support":
        support_page()

    if st.sidebar.button("Logout"):
        st.session_state.is_logged_in = False
        st.session_state.user_role = ""
        st.session_state.user_name = ""
        st.rerun()
