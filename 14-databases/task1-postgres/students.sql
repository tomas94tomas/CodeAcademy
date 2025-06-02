-- Create Students table
CREATE TABLE Students (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(100),
    Age INTEGER
);

-- Insert records
INSERT INTO Students (Name, Age) VALUES ('Jonas', 20);
INSERT INTO Students (Name, Age) VALUES ('Aiste', 22);
INSERT INTO Students (Name, Age) VALUES ('Lukas', 19);

-- Query all
SELECT * FROM Students;