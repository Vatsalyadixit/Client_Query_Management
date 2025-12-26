import pandas as pd
import streamlit as st
from db_connection import get_connection
from datetime import date
from Background_image import bg_image_2
from Background_image import bg_image_4


col1, col2 = st.columns([8,2]) # Setting up refresh button 

with col2:
    if st.button("🔁 Refresh"):
        st.rerun()

def support_page():

    theme = st.sidebar.segmented_control("Theme",["Dark","Light"]) # make a theme changer
    if theme == "Dark":
        bg_image_2()
    else:
        bg_image_4() 

    st.header("Support Dashboard")

    conn = get_connection()
    cursor = conn.cursor()

    tab1, tab2 = st.tabs(["Query Management", "Dashboard Analysis"])

    # ================= QUERY MANAGEMENT =================
    with tab1:

        filter_option = st.segmented_control(
            "Query Management",
            ["All", "Opened", "Closed"]
        )

        if filter_option == "All": # Selection of the query status
            cursor.execute("SELECT * FROM Query_DB")
        else:
            cursor.execute(
                "SELECT * FROM Query_DB WHERE status=%s",
                (filter_option,)
            )

        queries = cursor.fetchall()

        df = pd.DataFrame(
            queries,
            columns=[
                "query_id","email","mobile","heading",
                "description","status","opened","closed"
            ]
        )

        # Showing query count metrics
        st.metric("Open Queries", len(df[df["status"] == "Opened"]))
        st.metric("Closed Queries", len(df[df["status"] == "Closed"]))

        st.dataframe(df)

        if not df.empty: #setup of query update for support teams

            selected_id = st.selectbox(
                "Select Query ID",
                df["query_id"]
            )

            status = st.segmented_control(
                "Change Query Status",
                ["Close Query", "Open Query"]
            )

            if status == "Close Query":
                cursor.execute(
                    "UPDATE Query_DB SET status=%s, date_closed=%s WHERE query_id=%s",
                    ("Closed", date.today(), selected_id)
                )
                conn.commit()
                st.success("Query Closed")
                

            elif status == "Open Query":
                cursor.execute(
                    "UPDATE Query_DB SET status=%s, date_closed=%s WHERE query_id=%s",
                    ("Opened", None, selected_id)
                )
                conn.commit()
                st.success("Query Reopened")
                

    # ================= DASHBOARD ANALYSIS =================
    with tab2:

        cursor.execute("SELECT * FROM Query_DB")
        data = cursor.fetchall()

        df = pd.DataFrame(
            data,
            columns=[
                "query_id","email","mobile","heading",
                "description","status","opened","closed"
            ]
        )

        # Pie chart showing opened queries by type
        st.subheader("Opened Queries Distribution")

        opened_df = df[df["status"] == "Opened"]
        heading_count = opened_df["heading"].value_counts()

        if not heading_count.empty:
            st.pyplot(heading_count.plot.pie(autopct="%1.1f%%", ylabel="", title="Opened Queries by Heading").figure)

        # Support load monitoring
        st.subheader("Support Load Monitoring")
        st.write("Most Frequent Query Types")

        load_filter = st.selectbox("Select Query Status for Load Analysis",["All", "Opened", "Closed"])

        if load_filter == "All":
            load_df = df
        else:
            load_df = df[df["status"] == load_filter]

        if not load_df.empty:
            st.bar_chart(load_df["heading"].value_counts())
        else:
            st.info("No data available for selected filter")


        # Service efficiency analysis
        st.subheader("Queries Taking More Time to Resolve")

        resolved_df = df[df["closed"].notnull()].copy()

        if not resolved_df.empty:

            resolved_df["resolution_days"] = (pd.to_datetime(resolved_df["closed"]) - pd.to_datetime(resolved_df["opened"])).dt.days

            slow_queries = resolved_df.sort_values(by="resolution_days", ascending=False).head(5)

            st.bar_chart(slow_queries.set_index("heading")["resolution_days"])

    conn.close()
