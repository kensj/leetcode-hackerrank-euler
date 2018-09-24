SELECT MAX(Employee.Salary) as SecondHighestSalary
FROM Employee
WHERE Employee.Salary NOT IN
(
    SELECT MAX(Employee.Salary) as Salary
    FROM Employee
)