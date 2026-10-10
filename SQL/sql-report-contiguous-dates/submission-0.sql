WITH all_tasks AS (
    SELECT fail_date AS task_date, 'failed' AS period_state
    FROM failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL
    SELECT success_date AS task_date, 'succeeded' AS period_state
    FROM succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),
grouped AS (
    SELECT
        task_date,
        period_state,
        ROW_NUMBER() OVER (ORDER BY task_date) -
        ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY task_date) AS grp
    FROM all_tasks
)
SELECT
    period_state,
    MIN(task_date) AS start_date,
    MAX(task_date) AS end_date
FROM grouped
GROUP BY period_state, grp
ORDER BY start_date;