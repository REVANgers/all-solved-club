/* Write your PL/SQL query statement below */
/* reference 1 : https://leetcode.com/problems/all-people-report-to-the-given-manager/discuss/491341/Super-easy-greater-Hierarchical-query-in-ORACLE-avoiding-cycle! */
/* 1-1 */
/*
SELECT employee_id
FROM   Employees
WHERE  employee_id != 1
START WITH employee_id = 1
CONNECT BY NOCYCLE PRIOR employee_id = manager_id;
*/
/* 1-2 */
/*
SELECT employee_id
FROM   Employees
GROUP BY employee_id
HAVING employee_id != 1
START WITH employee_id = 1
CONNECT BY NOCYCLE PRIOR employee_id = manager_id;
*/
/* reference 2 : https://leetcode.com/problems/all-people-report-to-the-given-manager/discuss/447987/Oracle-86-faster */
/* 2-1 */
SELECT DISTINCT employee_id
FROM   Employees
WHERE  level > 1 and level < 5
START WITH employee_id = 1
CONNECT BY NOCYCLE PRIOR employee_id = manager_id;
