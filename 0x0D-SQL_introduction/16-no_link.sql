-- To Lists all records which having a name value
-- ordered by descending score.
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC
