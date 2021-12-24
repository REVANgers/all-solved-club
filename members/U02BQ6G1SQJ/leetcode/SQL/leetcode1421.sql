/* Write your PL/SQL query statement below */
SELECT q.id, q.year, NVL(n.npv, 0) AS npv
FROM   Queries q 
LEFT OUTER JOIN NPV n 
ON     q.id = n.id 
AND    q.year = n.year;
