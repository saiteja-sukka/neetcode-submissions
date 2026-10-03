SELECT d.name AS department, e.name AS employee, e.salary
FROM employee e
JOIN department d ON e.department_id = d.id
WHERE (e.department_id, e.salary) IN (
    SELECT department_id, MAX(salary)
    FROM employee
    GROUP BY department_id
);