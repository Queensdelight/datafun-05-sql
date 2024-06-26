# Datafun-05-sql

## Overview

This project integrates Python and SQL, focusing on database interactions using SQLite. It introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, 
including queries with joins, filters, and aggregations.

## Follow this steps to create your Resipotory

* GitHub Repository: datafun-05-sql or datafun-05-sql-project
* Documentation: README.md
* Initialize script: db_initialize_yourname.py
* Operations script: db_operations_yourname.py

## How to Install and Run the Project

External Dependencies: This project requires the following external modules, so a virtual environment is recommended.

* pandas
* pyarrow

## Version Control with Git

* Create a new GitHub repository.
* Clone the repository to your local machine.
* Document the steps and commands in your README.md.
* Document your workflow and commands as you edit, add, commit, and push changes to the GitHub repository.

## Objective

Create a Python script that demonstrates the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. Incorporate logging to document the process and provide user feedback.

### 1. Environment Setup

   1. Create and activate a Python virtual environment for the project.
   1. Install all required packages into your local project virtual environment.
   1. After installing the required dependencies, redirect the output of the pip freeze command to a requirements.txt file in your root project folder.
   1. Document the process and commands you used in your README.md.
   1. Add a .gitignore file to your project to exclude the virtual environment folder, your .vscode settings folder, and any other files that do not need to be committed to GitHub.
   

Terminal Commands: Windows example - record your process in your README:

```Powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install pandas pyarrow
py -m pip freeze > requirements.txt
```

Terminal Commands: Mac example - record your process in your README:

``` python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas pyarrow
python3 -m pip freeze > requirements.txt
```

### 2. Project Start

In your Python file, create a docstring with a brief introduction to your project.


### 3. Import Dependencies (At the Top, After the Introduction)

Organize your project imports near the top of the file, following conventions. 
For example, standard library imports first, then external library imports, then local module imports. 
Continue to practice importing your own modules and reuse your prior code when building your project folders. 
Follow conventional package import organization and aliasing. Import each package just once near the top of the file. 
Be sure you have INSTALLED any external packages (those not in the Python Standard Library) into your active project virtual 
environment first.

Note: if we use "import pathlib", we must use "pathlib.Path" when working with a Path. 
If you use "from pathlib import Path", you omit the initial pathlib in pathlib.Path, and just use Path.

### 4. Logging

Logging is recommended for most professional projects. 
Implement logging to enhance debugging and maintain a record of program execution.

1. Configure logging to write to a file named log.txt.
1. Log the start of the program using logging.info().
1. Log the end of the program using logging.info().
1. Log exceptions using logging.exception().
1. Log other major events using logging.info().
1. Log the start and end of major functions using logging.debug().

For example:

```python
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method
```

### 5. Schema Design and Database Creation

Design a schema with at least two related tables, including foreign key constraints. 
Document the schema design in your README.md.

Implement a Python script to create the database, create the tables, and populate the tables. 
Keep each SQL statement in a separate file.

For example:

```python

import sqlite3
import pandas as pd
import pathlib

# Your code here....

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
```

### 6. SQL Operations

Implement SQL statements and queries to perform additional operations and use Python to execute your SQL statements. 
You might create an additional table, insert new records, 
and perform data querying (with filters, sorting, and joining tables), 
data aggregation, and record update and deletion.

Include the following SQL files:

1. create_tables.sql - create your database schema using SQL
2. insert_records.sql - insert at least 10 additional records into each table.
3. update_records.sql - update 1 or more records in a table.
4. delete_records.sql - delete 1 or more records from a table.
5. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.
6. query_filter.sql - use WHERE to filter data based on conditions.
7. query_sorting.sql - use ORDER BY to sort data.
8. query_group_by.sql - use GROUP BY clause (and optionally with aggregation)
9. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.


### 7. Python and SQL Integration

Use Python to interact with the SQL database and execute SQL commands:

```python
import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
```


### 8. Define Main Function for SQL Operations Script

Implement a main() function to execute the project SQL operations logic.

```python
def main():
    db_filepath = 'your_database.db'

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")

```


### 9. Conditional Script Execution

Ensure the main function only executes when the script is run directly, 
not when imported as a module by using standard boilerplate code.


## Module Design

- Include a docstring at the top of the file describing its purpose.
- The code should be clear, well-organized, and demonstrate good practices.
- Include comments and docstrings for clarity.


- - -
© 2024 Copyright ownership Dr. Denise Case. All Rights Reserved.











