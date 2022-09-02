 /*
 
 Написать запрос для получения следующих данных: 

	- Название альбома, 

	- Жанр альбома, 

	- Название группы или имя артиста, 

	- Длительнось альбома выраженная в минутах (для округления может понадобиться 

		функция ROUND. Применяется точно так же как и в Python)

	- Размер альбома выраженый в Мегабайтах

	- Количество треков входящих в альбом

Указанные данные надо посчитать только для медиа-типа "MPEG audio file". Полученый

результат отсортировать по жанру и артистам.


Примерный результат представлен на скрине. Название колонок и их порядок в результате 

должны соответствовать названиям и порядку указанным на скрине.
 
 */
 
 
 SELECT al.Title AS 'Album name', gen.Name AS 'Genre', art.Name AS 'Artist or Group',
 		ROUND(SUM(tr.Milliseconds) * 0.0000166667) AS 'Duration(Minutes)',
 		ROUND(SUM(tr.Bytes) / 1048576)  AS 'Size(Mb)',
 		SUM(tr.UnitPrice) AS 'Album price',
 		COUNT(tr.AlbumId) AS 'Count tracks'
 FROM tracks AS tr
 JOIN media_types AS mt ON tr.MediaTypeId = mt.MediaTypeId
 JOIN genres AS gen ON tr.GenreId = gen.GenreId
 JOIN albums AS al ON tr.AlbumId = al.AlbumId
 JOIN artists AS art ON al.ArtistId = art.ArtistId
 WHERE mt.Name = 'MPEG audio file' AND tr.AlbumId IS NOT NULL GROUP BY tr.AlbumId ORDER BY gen.Name, art.Name;
