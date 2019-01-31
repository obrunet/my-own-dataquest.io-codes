## 3. Psycopg2 ##

# Import the psycopg2 library.
import psycopg2

# connects to the dq database with the user dq.
conn = psycopg2.connect("dbname=dq user=dq")
# initializes a Cursor object from the connection
cur = conn.cursor()
# displays the Cursor object.
print(cur)
# closes the Connection using the close method.
conn.close()

## 4. Creating a table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
# SQL query that creates a table called notes in the dq db
query = """
CREATE TABLE notes (
    id integer PRIMARY KEY,
    body text,
    tittle text
);
"""
cur.execute(query)
cur.close()

## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
query = """
CREATE TABLE notes (
    id integer PRIMARY KEY,
    body text,
    title text
);
"""
cur.execute(query)
conn.commit()
conn.close()


## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
# Set the autocommit property of the Connection object to True.
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE facts(id integer PRIMARY KEY, country text, value text)")
conn.close()

## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
conn.commit()
cur.execute("SELECT * from notes;")
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE income OWNER dq;")
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("DROP DATABASE income;")
conn.close()