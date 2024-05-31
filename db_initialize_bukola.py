''' This project create a Python script that demonstrates the ability to interact with a SQL database, 
including creating a database, defining a schema, and executing various SQL commands. 
Incorporate logging to document the process and provide user feedback.
'''

import sqlite3
import logging
import pandas as pd

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        logging.info(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
    return conn

def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        logging.info("Table created successfully")
    except sqlite3.Error as e:
        logging.error(f"Error creating table: {e}")

def insert_data(conn, insert_sql, data):
    """Insert data into the table."""
    try:
        c = conn.cursor()
        c.executemany(insert_sql, data)
        conn.commit()
        logging.info("Data inserted successfully")
    except sqlite3.Error as e:
        logging.error(f"Error inserting data: {e}")

def query_data(conn, query_sql):
    """Query data from the table."""
    try:
        df = pd.read_sql_query(query_sql, conn)
        logging.info("Data queried successfully")
        logging.info(f"\n{df}")
    except sqlite3.Error as e:
        logging.error(f"Error querying data: {e}")

def main():
    database = "test.db"

    sql_create_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        published_date TEXT,
        isbn TEXT
    );
    """

    sql_insert_data = """
    INSERT INTO books (title, author, published_date, isbn) VALUES (?, ?, ?, ?);
    """

    books_data = [
        ('To Kill a Mockingbird', 'Harper Lee', '1960', '978-0061120084'),
        ('1984', 'George Orwell', '1949', '978-0451524935'),
        ('Pride and Prejudice', 'Jane Austen', '1813', '978-1503290563'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', '1925', '978-0743273565')
    ]

    sql_query_data = "SELECT * FROM books;"

    # Create a database connection
    conn = create_connection(database)

    # Create table
    if conn is not None:
        create_table(conn, sql_create_table)

        # Insert data
        insert_data(conn, sql_insert_data, books_data)

        # Query data
        query_data(conn, sql_query_data)

        # Close the connection
        conn.close()
        logging.info("Database connection closed")
    else:
        logging.error("Error! Cannot create the database connection.")

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('project.db')

# Create a cursor object
cur = conn.cursor()

# Create Movies table
cur.execute('''
CREATE TABLE Movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    release_year INTEGER,
    director_id INTEGER,
    FOREIGN KEY (director_id) REFERENCES Directors(id)
)
''')

# Create Actors table
cur.execute('''
CREATE TABLE Actors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthdate TEXT
)
''')

# Create Directors table
cur.execute('''
CREATE TABLE Directors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthdate TEXT
)
''')

# Create Genres table
cur.execute('''
CREATE TABLE Genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT NOT NULL
)
''')

# Create Movie_Actors table (many-to-many relationship between Movies and Actors)
cur.execute('''
CREATE TABLE Movie_Actors (
    movie_id INTEGER,
    actor_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (actor_id) REFERENCES Actors(id),
    PRIMARY KEY (movie_id, actor_id)
)
''')

# Create Movie_Genres table (many-to-many relationship between Movies and Genres)
cur.execute('''
CREATE TABLE Movie_Genres (
    movie_id INTEGER,
    genre_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES Movies(id),
    FOREIGN KEY (genre_id) REFERENCES Genres(id),
    PRIMARY KEY (movie_id, genre_id)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")


if __name__ == '__main__':
    main()
