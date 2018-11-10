CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N = N-1;
  RETURN (
      SELECT
      (SELECT DISTINCT E.Salary
      FROM Employee E
      ORDER BY E.Salary DESC
      LIMIT 1 OFFSET N)
      AS getNthHighestSalary  
  );
END