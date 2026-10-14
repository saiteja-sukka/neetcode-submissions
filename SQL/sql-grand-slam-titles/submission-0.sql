SELECT 
    p.player_id,
    p.player_name,
    SUM(
        (p.player_id = c.wimbledon)::int +
        (p.player_id = c.fr_open)::int +
        (p.player_id = c.us_open)::int +
        (p.player_id = c.au_open)::int
       ) AS grand_slams_count
FROM players p
JOIN championships c
    ON p.player_id = c.wimbledon
    OR p.player_id = c.fr_open
    OR p.player_id = c.us_open
    OR p.player_id = c.au_open
GROUP BY p.player_id, p.player_name;