-- Counts records by score, orders by number descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;

