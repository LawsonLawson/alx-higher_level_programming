-- This script list all shows contained in the `hbtn_0d_tvshows` database
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows LEFT JOIN tv_shows_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
