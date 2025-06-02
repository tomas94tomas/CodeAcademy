CREATE TABLE Authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INTEGER REFERENCES Authors(id)
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE BorrowedBooks (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    book_id INTEGER REFERENCES Books(id),
    borrowed_date DATE NOT NULL,
    returned_date DATE
);