## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
#  returns the schema of the facts table and assign the resulting list of tuples
schema = conn.execute("PRAGMA table_info(facts);").fetchall()
for elt in schema:
    print (elt)

## 3. Explain query plan ##

query_plan_one = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE area > 40000;").fetchall()
query_plan_two = conn.execute("EXPLAIN QUERY PLAN SELECT area FROM facts WHERE area > 40000;").fetchall()
query_plan_three = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE name ='Czech Republic';").fetchall()
print(query_plan_one)
print(query_plan_two)
print(query_plan_three)

## 5. Time complexity ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query_plan_four = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE id=20;").fetchall()
print(query_plan_four)

## 9. All together now ##

query_plan_six = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000;").fetchall()
print(query_plan_six)
# creates an index for the population column in the facts table named pop_idx
conn.execute("CREATE INDEX IF NOT EXISTS pop_idx ON facts(population);")
# returns the query plan
query_plan_seven = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 10000;").fetchall()
print(query_plan_seven)