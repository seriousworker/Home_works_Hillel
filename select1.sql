SELECT t.Name AS 'Name of the track', COUNT(ii.TrackId) AS 'Ordered times',  SUM(ii.UnitPrice) AS 'Total in cash'
FROM invoice_items AS ii
JOIN tracks AS t ON ii.TrackId = t.TrackId
GROUP BY ii.TrackId;
