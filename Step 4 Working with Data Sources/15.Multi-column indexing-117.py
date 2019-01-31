## 2. Query Plan ##

import sqlite3
conn = sqlite3.connect("factbook.db")
query_plan_one = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.5 ;").fetchall()
print (query_plan_one)

## 3. Query plan for multi-column queries ##

conn = sqlite3.connect("factbook.db")
conn.execute("CREATE INDEX pop_idx ON facts(population);")
conn.execute("CREATE INDEX pop_growth_idx ON facts(population_growth);")
query_plan_two = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.05;").fetchall()
print(query_plan_two)

## 6. Creating a multi-column index ##

conn = sqlite3.connect("factbook.db")

# the first column in the parentheses becomes the primary key for the index
conn.execute("CREATE INDEX pop_pop_growth_idx ON facts(population, population_growth);")
query_plan_three = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM facts WHERE population > 1000000 AND population_growth < 0.05;").fetchall()
print(query_plan_three)

## 7. Covering index ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_four = conn.execute("EXPLAIN QUERY PLAN SELECT population, population_growth FROM facts WHERE population > 1000000  AND population_growth < 0.05;").fetchall()
print(query_plan_four)
# When an index contains all of the information necessary to answer a query, it's called a covering index. Since the index covers for the actual table and can return the requested results to the query, SQLite doesn't need to query the actual table. For many queries, especially as your data gets larger, this can be much more efficient.

## 8. Covering index for single column ##

conn = sqlite3.connect("factbook.db")
conn.execute("create index if not exists pop_pop_growth_idx on facts(population, population_growth);")
query_plan_five = conn.execute("EXPLAIN QUERY PLAN SELECT population FROM facts WHERE population > 1000000;").fetchall()
print(query_plan_five)