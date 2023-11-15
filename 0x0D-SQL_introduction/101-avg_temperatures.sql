-- To Displays average temperature F° Gouped by city and Ordered by descending temp
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
