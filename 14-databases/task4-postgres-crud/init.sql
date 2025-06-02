-- INSERT sample data
INSERT INTO Authors (name) VALUES ('George Orwell');
INSERT INTO Authors (name) VALUES ('Haruki Murakami');

INSERT INTO Books (title, author_id) VALUES ('1984', 1);
INSERT INTO Books (title, author_id) VALUES ('Kafka on the Shore', 2);

INSERT INTO Users (name, email) VALUES ('Tomas', 'tomas@example.com');
INSERT INTO Users (name, email) VALUES ('Laura', 'laura@example.com');

INSERT INTO BorrowedBooks (user_id, book_id, borrowed_date) VALUES (1, 1, CURRENT_DATE);

-- SELECT data
SELECT * FROM Books;
SELECT * FROM BorrowedBooks;

-- UPDATE data
UPDATE BorrowedBooks SET returned_date = CURRENT_DATE WHERE user_id = 1 AND book_id = 1;

-- DELETE example
DELETE FROM Users WHERE name = 'Laura';
