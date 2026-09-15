import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",  # <-- Apna MySQL Password yahan likhein
        database="library_db"
    )
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,
        contact VARCHAR(20),
        address TEXT,
        role VARCHAR(50) NOT NULL
    )
    """)

    # Books Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        isbn VARCHAR(50),
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        category VARCHAR(100),
        price DECIMAL(10, 2),
        copies INT DEFAULT 1,
        cover_image VARCHAR(255)
    )
    """)

    # Borrowed Books Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS borrowed_books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        book_title VARCHAR(255) NOT NULL,
        student_name VARCHAR(100) NOT NULL,
        roll_no VARCHAR(50) NOT NULL,
        department VARCHAR(100),
        email VARCHAR(100),
        phone_number VARCHAR(20),
        issue_datetime VARCHAR(100),
        due_date VARCHAR(50),
        status VARCHAR(50) DEFAULT 'Issued'
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("MySQL Database Initialized Successfully!")

if __name__ == "__main__":
    init_db()