import pandas as pd 
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

query = "CREATE DATABASE IF NOT EXISTS CQM" # CREATED A NEW DATABASE
cursor.execute(query)

query_1 = "USE CQM"
cursor.execute(query_1)

query_2 = """CREATE TABLE IF NOT EXISTS user_logs (
             user_name VARCHAR(255) PRIMARY KEY,
             password VARCHAR(255),
             role VARCHAR(50)
            );"""
cursor.execute(query_2) # CREATED A TABLE TO STORE LOGIN DEATILS OF THE USER

query_3 = """CREATE TABLE IF NOT EXISTS Query_DB (
            query_id VARCHAR(50) PRIMARY KEY,
            client_email VARCHAR(255),
            client_mobile VARCHAR(20),
            query_heading VARCHAR(100),
            query_description VARCHAR(255),
            status VARCHAR(20),
            date_opened DATE,
            date_closed DATE
            );"""
cursor.execute(query_3) # REATED A TABLE TO STORE QUERIES OF THE CLEINT

path = r"E:\GUVI_DS\Projects\Client_Query_Management\synthetic_client_queries.csv"
df = pd.read_csv(path) # READING THE QUERY FILE AND CREATING A DATAFRAME
df["date_closed"] = df["date_closed"].where(df["date_closed"].notnull(), None) # ASSINGING THE VALUES TO THE DATAECLOSED COLUMN 


query_4 = """INSERT INTO Query_DB 
(query_id, client_email, client_mobile, query_heading, query_description, status, date_opened, date_closed)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
for index, row in df.iterrows(): #INSERTING DATA IN THE TABLE BY LOOPING THE DATA FRAME
    values = (
        row["query_id"],
        row["client_email"],
        row["client_mobile"],
        row["query_heading"],
        row["query_description"],
        row["status"],
        row["date_opened"],
        row["date_closed"]
    )
    cursor.execute(query_4, values) #UPDATE THE OLD QUERIES DATA INTO THE QUERY TABLE 

conn.commit()

print("CSV data inserted successfully!")
cursor.close()
conn.close()