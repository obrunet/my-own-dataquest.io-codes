## 3. Connecting to the Database ##

import sqlite3

# connects to jobs.db, and assign the Connection instance
conn = sqlite3.connect("jobs.db")

## 6. Creating a Cursor and Running a Query ##

import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# basic select query that return all of the values & store this query as a string named query
query = "select * from recent_grads;"

# uses the Cursor method execute() to run the query against our database
cursor.execute(query)

# rReturns the full results set and store it
results = cursor.fetchall()

# prints the first three tuples in the list
print(results[0:2])

# --------------- other example --------------

# query that returns all of the values in the Major column from the recent_grads table
other_query = "select Major from recent_grads;"
cursor.execute(other_query)
majors = cursor.fetchall()
print(majors[:2])

## 8. Fetching a Specific Number of Results ##

import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select Major, Major_category from recent_grads;"
cursor.execute(query)
five_results = cursor.fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

# Because SQLite restricts access to the database file when we're connected to a database, we need to close the connection when we're done working with it. Closing the connection allows other processes to access the database, which is important when you're in a production environment and working with other team members.

## 10. Practice ##

import sqlite3

conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()

query = "select Major from recent_grads order by Major desc;"
cursor.execute(query)
reverse_alphabetical = cursor.fetchall()

conn.close()