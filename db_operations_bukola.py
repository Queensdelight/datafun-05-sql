import sqlite3
import pandas as pd
import pathlib
import logging

# Define the database file in the current root project directory
db_file = pathlib.Path("project.sqlite3")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)



def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)


def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

# Define function for inserting new records to the data tables
def execute_insert_records(db_file, insert_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        insert_records_sql_file = pathlib.Path("insert_records.sql")
        with open(insert_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {insert_records_sql_file}")

# Define function for deleting records from the data tables
def execute_delete_records(db_file, delete_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        delete_records_sql_file = pathlib.Path("delete_records.sql")
        with open(delete_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {delete_records_sql_file}")

# Define function for updating records from the data tables
def execute_update_records(db_file, update_records_sql_file):
    with sqlite3.connect(db_file) as conn:
        update_records_sql_file = pathlib.Path("update_records.sql")
        with open(update_records_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {update_records_sql_file}")


# Define function for performing operations on data from tables
def execute_query_aggregation(db_file, query_aggregation_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_aggregation_sql_file = pathlib.Path("query_aggregation.sql")
        with open(query_aggregation_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_aggregation_sql_file}")

# Define function for filtering data from tables
def execute_query_filter(db_file, query_filter_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_filter_sql_file = pathlib.Path("query_filter.sql")
        with open(query_filter_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_filter_sql_file}")

# Define function for combining data from 2 tables
def execute_query_join(db_file, query_join_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_join_sql_file = pathlib.Path("query_join.sql")
        with open(query_join_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_join_sql_file}")

# Define function for sorting data in tables
def execute_query_sorting(db_file, query_sorting_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_sorting_sql_file = pathlib.Path("query_sorting.sql")
        with open(query_sorting_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_sorting_sql_file}")

# Define function for grouping data from tables
def execute_query_group_by(db_file, query_group_by_sql_file):
    with sqlite3.connect(db_file) as conn:
        query_group_by_sql_file = pathlib.Path("query_group_by.sql")
        with open(query_group_by_sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {query_group_by_sql_file}")



def main():
    create_database()
    create_tables()
    insert_data_from_csv()
    execute_query_group_by()
    execute_query_sorting()
    execute_query_join()
    execute_query_filter()
    execute_query_aggregation()
    execute_update_records()
    execute_delete_records()
    

if __name__ == "__main__":
    logging.info("Program started") # add this at the beginning of the main method
    main()
    logging.info("Program ended")  # add this at the end of the main method
