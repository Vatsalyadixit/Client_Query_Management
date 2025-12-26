import streamlit as st
from db_connection import get_connection
from datetime import date
from Background_image import bg_image_2
from Background_image import bg_image_4


col1, col2 = st.columns([8,2]) # Setting up refresh button 

with col2:
    if st.button("🔁 Refresh"):
        st.rerun()

def client_page(username):

    theme = st.sidebar.segmented_control("Theme",["Dark","Light"]) # make a theme changer
    if theme == "Dark":
        bg_image_2()
    else:
        bg_image_4() 
    st.header("Submit Query")

    conn = get_connection()
    cursor = conn.cursor()

    # Fetching client email from user_logs
    cursor.execute(
        "SELECT user_name FROM user_logs WHERE user_name=%s",
        (username,)
    )
    email = cursor.fetchone()[0]

    # Generate next query_id
    cursor.execute(
        "SELECT query_id FROM Query_DB ORDER BY query_id DESC LIMIT 1"
    )
    last_id = cursor.fetchone()

    if last_id: # Extracting last query number from the database  
        last_number = int(last_id[0].replace("Q", ""))
        query_id = f"Q{last_number + 1}"
    else:
        query_id = "Q1"

    conn.close()

    # Receving inputs form users 
    email_input = st.text_input("Email", email)
    mobile = st.text_input("Mobile", max_chars=10)
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    # Inserting query into query_db
    if st.button("Submit"):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Query_DB
            (query_id, client_email, client_mobile, query_heading,
             query_description, status, date_opened, date_closed)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                query_id,
                email_input,
                mobile,
                heading,
                description,
                "Opened",
                date.today(),
                None
            )
        )

        conn.commit()
        conn.close()

        st.success(f"Query submitted successfully")
