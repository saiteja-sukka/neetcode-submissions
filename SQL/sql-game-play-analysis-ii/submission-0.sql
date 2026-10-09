SELECT player_id, device_id
FROM (
    SELECT player_id, device_id, ROW_NUMBER() OVER (PARTITION BY player_id ORDER BY event_date) AS rn
    FROM activity
) ranked
WHERE rn = 1;