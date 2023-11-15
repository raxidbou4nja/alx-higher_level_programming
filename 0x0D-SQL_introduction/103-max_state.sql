-- To Display the max temperature of each state and order them by state name.
SELECT `state`, MAX(`value`) AS `max_temp` FROM `temperatures` GROUP BY `state` ORDER BY `state`;
