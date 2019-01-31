## 1. The psql tool ##

/home/dq$ psql

## 2. Running SQL queries ##

## creates a database called bank_accounts
/home/dq$ psql
CREATE DATABASE bank_accounts;

## 3. Special PostgreSQL commands ##

## lists all available databases
/home/dq$ psql
\l

## 4. Switching databases ##

/home/dq$ psql -d bank_accounts
## creates a table called deposits in bank_accounts
CREATE TABLE deposits (
    id integer PRIMARY KEY,
    name text,
    amount float
);
## uses the \dt command to list all of the tables in bank_accounts.
\dt
## Exit psql.
\q

## 5. Creating users ##

## creates a user called sec
/home/dq$ psql
CREATE ROLE sec WITH LOGIN CREATEDB PASSWORD 'test';

## 6. Adding permissions ##

/home/dq$ psql -d bank_accounts
## grants all privileges on the table deposits to the user sec.
GRANT ALL PRIVILEGES ON deposits TO sec;
## lists all the privileges for deposits using \dp.
\dp

## 7. Removing permissions ##

/home/dq$ psql -d bank_accounts
## revokes all privileges on the table deposits from the user sec
REVOKE ALL PRIVILEGES ON deposits FROM sec;

## 8. Superusers ##

/home/dq$ psql
## creates a user called aig with the following modifying statements:
CREATE ROLE aig WITH LOGIN PASSWORD 'test' SUPERUSER;
## lists all the users using \du.
\du