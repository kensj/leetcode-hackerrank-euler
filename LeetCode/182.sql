SELECT P.Email AS Email
FROM Person P
GROUP BY P.Email
HAVING COUNT(P.Email) > 1