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


--вывести все данные по фильмам с рейтингом больше 8, выпущенным с 1970 по 1979
SELECT * FROM movies
WHERE imdb_rating > 8
	AND year BETWEEN 1970 AND 1979;
	
	
	
--выведите данные о то-3 фильмов (с наибольшим рейтингом)
SELECT * 
FROM movies
WHERE imdb_rating IS NOT NULL
ORDER BY imdb_rating DESC
LIMIT 3;
