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