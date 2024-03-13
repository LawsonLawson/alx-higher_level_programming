-- This script lists all the cities found in a database `hbtn_0d_usa`
SELECT cities.id, cities.name, states.name
FROM states JOIN cities
WHERE cities.state_id = state.id
ORDER BY cities.id ASC;
