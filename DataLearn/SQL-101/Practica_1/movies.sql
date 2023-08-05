--вывести названия только тех фильмов у которых заполнен рейтинг
SELECT name
FROM movies
WHERE imdb_rating IS NOT NULL;


--выведите все даные о фильмах, выпущеных с 1990 по 1999
SELECT * FROM movies
WHERE year BETWEEN 1990 AND 1999;
--(year >= 1990) AND (year <= 1999);


--вывести данные о фильмах, чье название начинается на буквы с A - J
SELECT * FROM movies
WHERE name ~ '^[A-J]';
--WHERE name BETWEEN 'A' AND 'J'


