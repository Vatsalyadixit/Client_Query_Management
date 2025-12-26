# Client Query Management System

A role based **Client Query Management System** built using **Python, Streamlit, and MySQL**.  
This application allows clients to submit queries and support teams to manage, analyze, and resolve them through an interactive dashboard.

---

## 🔹 Project Overview

This project is designed to simulate a real world customer support system where:
- Clients can raise queries
- Support teams can track, update, and resolve queries
- Management-level dashboards provide analytics and service insights

The application uses **Streamlit**, which combines frontend and backend logic within a single Python codebase.

---

## 🔹 Features

### Client Side
- Secure signup and login
- Submit support queries
- Auto filled user details
- View submitted queries

### Support Side
- View all client queries
- Filter queries by status (All / Opened / Closed)
- Update query status (Open ↔ Closed)
- Refresh data in real time

### Dashboard & Analytics
- Open vs Closed query overview
- Most frequent query types
- Support load monitoring
- Queries taking the longest time to resolve
- Data driven insights for service efficiency

---

## 🔹 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** MySQL  
- **Data Handling:** Pandas  
- **Visualization:** Streamlit charts  

---

## 🔹 Project Structure

Client_Query_Management/
│
├── web_page.py # Main Streamlit application
├── auth.py # Login and signup logic
├── client_page.py # Client-side functionality
├── support_page.py # Support dashboard and analytics
├── db_connection.py # MySQL database connection
├── query_db.py # MySQL query database configuration 
├── synthetic_client_queries.csv # query data file
├── Background_image.py # Application Theme setup file
├── images/
│ ├── background_img.jpg
│ ├── background_img_2.jpg
│ ├── background_img_3.jpg
│ └── background_img_4.jpg
└── README.md

---

## 🔹 How to Run the Project

1. Clone the repository
2. Install required packages:
pip install streamlit pandas mysql-connector-python

3. Configure MySQL database and tables
4. Run the application:
streamlit run web_page.py

---

## 🔹 Use Cases

- Customer support management systems
- Ticket/query tracking platforms
- Learning role based dashboards
- Real time analytics with Streamlit

---

## 🔹 Future Enhancements

- SLA-based query prioritization (Fast / Slow)
- Email notifications
- Admin-level dashboard

---

## 👤 Author

**Vatsalya Dixit**  
Python | Data Analytics | Streamlit | MySQL
