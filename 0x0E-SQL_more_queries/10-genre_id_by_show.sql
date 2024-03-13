-- This is a script that lists all shows in `hbtn_0d_tvshows which have at least one genre.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows JOIN tv_show_genres
WHERE tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
