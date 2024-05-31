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
