# More SQL queries

## Project Learnings
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

## Tasks

- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server.

- Write a script that creates the MySQL server user user_0d_1.
  - user_0d_1 should have all privileges on your MySQL server
  - The user_0d_1 password should be set to user_0d_1_pwd
  - If the user user_0d_1 already exists, your script should not fail

- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
  - user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
  - The user_0d_2 password should be set to user_0d_2_pwd
  - If the database hbtn_0d_2 already exists, your script should not fail
  - If the user user_0d_2 already exists, your script should not fail

- Write a script that creates the table force_name on your MySQL server.
  - force_name description:
    - id INT
    - name VARCHAR(256) can’t be null
    - The database name will be passed as an argument of the mysql command
    - If the table force_name already exists, your script should not fail

- Write a script that creates the table id_not_null on your MySQL server.
  - id_not_null description:
    - id INT with the default value 1
    - name VARCHAR(256)
    - The database name will be passed as an argument of the mysql command
    - If the table id_not_null already exists, your script should not fail

- Write a script that creates the table unique_id on your MySQL server.
  - unique_id description:
    - id INT with the default value 1 and must be unique
    - name VARCHAR(256)
    - The database name will be passed as an argument of the mysql command
    - If the table unique_id already exists, your script should not fail

- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
  - states description:
    - id INT unique, auto generated, can’t be null and is a primary key
    - name VARCHAR(256) can’t be null
    - If the database hbtn_0d_usa already exists, your script should not fail
    - If the table states already exists, your script should not fail

- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
  - cities description:
    - id INT unique, auto generated, can’t be null and is a primary key
    - state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
    - name VARCHAR(256) can’t be null
    - If the database hbtn_0d_usa already exists, your script should not fail
    - If the table cities already exists, your script should not fail

- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
  - The states table contains only one record where name = California (but the id can be different, as per the example)
  - Results must be sorted in ascending order by cities.id
  - You are not allowed to use the JOIN keyword
  - The database name will be passed as an argument of the mysql command

- Write a script that lists all cities contained in the database hbtn_0d_usa.
  - Each record should display: cities.id - cities.name - states.name
  - Results must be sorted in ascending order by cities.id
  - You can use only one SELECT statement
  - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
  - Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
    - Each record should display: tv_shows.title - tv_show_genres.genre_id
    - Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
  - Write a script that lists all shows contained in the database hbtn_0d_tvshows.
    - Each record should display: tv_shows.title - tv_show_genres.genre_id
    - Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    - If a show doesn’t have a genre, display NULL
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)
  - Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
    - Each record should display: tv_shows.title - tv_show_genres.genre_id
    - Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)
  - Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
    - Each record should display: tv_genres.name - number of shows
    - Don’t display a genre that doesn’t have any shows linked
    - Results must be sorted in descending order by the number of shows linked
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 13-count_shows_by_genre.sql)
  - Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
    - The tv_shows table contains only one record where title = Dexter (but the id can be different)
    - Each record should display: tv_genres.name
    - Results must be sorted in ascending order by the genre name
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 14-my_genres.sql)
  - Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.
    - The tv_genres table contains only one record where name = Comedy (but the id can be different)
    - Each record should display: tv_shows.title
    - Results must be sorted in ascending order by the show title
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 15-comedy_only.sql)
  - Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
    - If a show doesn’t have a genre, display NULL in the genre column
    - Each record should display: tv_shows.title - tv_genres.name
    - Results must be sorted in ascending order by the show title and genre name
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 16-shows_by_genre.sql)
  - Write a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
    - The tv_shows table contains only one record where title = Dexter (but the id can be different)
    - Each record should display: tv_genres.name
    - Results must be sorted in ascending order by the genre name
    - You can use a maximum of two SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 100-not_my_genres.sql)
  - Write a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
    - The tv_genres table contains only one record where name = Comedy (but the id can be different)
    - Each record should display: tv_shows.title
    - Results must be sorted in ascending order by the show title
    - You can use a maximum of two SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database hbtn_0d_tvshows_rate dump to your MySQL server: download
  - Write a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
    - Each record should display: tv_shows.title - rating sum
    - Results must be sorted in descending order by the rating
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command

- Import the database dump from hbtn_0d_tvshows_rate to your MySQL server: download (same as 102-rating_shows.sql)
  - Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
    - Each record should display: tv_genres.name - rating sum
    - Results must be sorted in ascending order by their rating
    - You can use only one SELECT statement
    - The database name will be passed as an argument of the mysql command