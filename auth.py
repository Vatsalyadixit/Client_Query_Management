import hashlib
from db_connection import get_connection

def hash_password(password): # Encoding the password and storing 
    return hashlib.sha256(password.encode()).hexdigest()

def signup(username, password, role):
    # Role validation with correct mail id
    if role == "client" and "@guvi" in username.lower():    
        return "Please signup with a valid mail id"

    if role == "support" and "@guvi" not in username.lower():
        return "Please signup with a valid work mail id"

    hashed_password = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()

    # Updating the database of user_logs with the new users
    cursor.execute(
        "insert into user_logs (user_name, password, role) values (%s, %s, %s)",
        (username, hashed_password, role)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return "Signup successful"

def login(username, password, role):    
    
    # Role validation with correct mail id
    if role == "client" and "@guvi" in username.lower():     
        return "Please log-in with a valid mail id"

    if role == "support" and "@guvi" not in username.lower():
        return "Please log-in with a valid work mail id"

    hashed_password = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()

    # Matching the user inputs with database values
    cursor.execute(
        "Select role from user_logs where user_name=%s and password=%s",
        (username, hashed_password)
    )

    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        return result[0], "Login successful"
    else:
        return None, "Invalid username or password"

