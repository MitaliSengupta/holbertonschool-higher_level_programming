-- script that list all genres from tv show and display number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
