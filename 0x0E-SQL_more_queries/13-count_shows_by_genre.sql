-- This is a script that lists all genres from the `hbtn_0d_tvshows` database and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM genres g
JOIN shows_genres sg ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
