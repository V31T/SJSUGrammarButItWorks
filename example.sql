CREATE TABLE Employees (EmployeeID INT, FirstName VARCHAR(50), LastName VARCHAR(50), BirthDate DATE );
INSERT INTO Employees (EmployeeID, FirstName, LastName, BirthDate) VALUES (1, 'John', 'Doe', '1990-01-15'), (2, 'Jane', 'Smith', '1985-05-20');
SELECT EmployeeID, FirstName, LastName FROM Employees WHERE BirthDate > '1980-01-01';
DROP TABLE Employees;

