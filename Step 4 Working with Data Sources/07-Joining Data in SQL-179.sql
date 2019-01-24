## 1. Introducing Joins ##

SELECT * FROM facts
INNER JOIN cities ON cities.facts_id = facts.id
LIMIT 10

## 2. Understanding Inner Joins ##

SELECT c.*, f.name AS country_name
FROM facts AS f
INNER JOIN cities AS c ON c.facts_id = f.id
LIMIT 5

## 3. Practicing Inner Joins ##

SELECT f.name AS country, c.name AS capital_city
FROM facts AS f
INNER JOIN cities AS c ON f.id = c.facts_id
WHERE c.capital = 1

## 4. Left Joins ##

SELECT f.name AS country, f.population 
FROM facts AS f
LEFT JOIN cities AS c ON f.id = c.facts_id
WHERE c.facts_id IS NULL

## 6. Finding the Most Populous Capital Cities ##

SELECT c.name as capital_city, f.name as country, c.population
FROM facts as f
INNER JOIN cities as c ON f.id = c.facts_id
WHERE c.capital = 1
ORDER BY c.population DESC
LIMIT 10

## 7. Combining Joins with Subqueries ##

SELECT c.name as capital_city, f.name as country, c.population
FROM facts as f
INNER JOIN
(
SELECT * FROM cities as c 
WHERE c.population > 10000000 AND c.capital = 1
) 
AS C ON f.id = c.facts_id
ORDER BY c.population DESC

## 8. Challenge: Complex Query with Joins and Subqueries ##

SELECT  f.name as country, urban_pop, 
        f.population as total_pop, 
        CAST(urban_pop as FLOAT) / CAST(f.population as FLOAT) as urban_pct
FROM facts as f

INNER JOIN
    (
SELECT SUM(c.population) as urban_pop, facts_id
FROM cities as c
GROUP BY facts_id
    ) AS c
ON f.id = c.facts_id

WHERE urban_pct > 0.5
ORDER BY urban_pct ASC