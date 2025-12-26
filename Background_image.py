import streamlit as st
import base64

## dark Theme
# Adding background image for first screen
def bg_image_1():
    with open(r"E:\GUVI_DS\Projects\Client_Query_Management\Theme\background_img.jpg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Adding background image after login
def bg_image_2():
    with open(r"E:\GUVI_DS\Projects\Client_Query_Management\Theme\background_img_2.JPG", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

##Light Theme
# Adding background image for first screen
def bg_image_3():
    with open(r"E:\GUVI_DS\Projects\Client_Query_Management\Theme\background_img_3.jpg", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Adding background image after login
def bg_image_4():
    with open(r"E:\GUVI_DS\Projects\Client_Query_Management\Theme\background_img_4.JPG", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )