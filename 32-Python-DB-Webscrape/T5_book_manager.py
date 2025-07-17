from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Set up database and ORM
Base = declarative_base()
engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)

def add_book(title, author):
    session = Session()
    book = Book(title=title, author=author)
    session.add(book)
    session.commit()
    session.close()
    print(f"Book '{title}' by {author} added.")

def view_books():
    session = Session()
    books = session.query(Book).all()
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book.id}: {book.title} by {book.author}")
    session.close()

def update_book(book_id, new_title, new_author):
    session = Session()
    book = session.query(Book).get(book_id)
    if book:
        book.title = new_title
        book.author = new_author
        session.commit()
        print(f"Book {book_id} updated.")
    else:
        print("Book not found.")
    session.close()

def delete_book(book_id):
    session = Session()
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        print(f"Book {book_id} deleted.")
    else:
        print("Book not found.")
    session.close()

def main():
    while True:
        print("\nBook Manager: [1] Add  [2] View  [3] Update  [4] Delete  [5] Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            add_book(title, author)
        elif choice == "2":
            view_books()
        elif choice == "3":
            book_id = int(input("Book ID to update: "))
            title = input("New title: ")
            author = input("New author: ")
            update_book(book_id, title, author)
        elif choice == "4":
            book_id = int(input("Book ID to delete: "))
            delete_book(book_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
