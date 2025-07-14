from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Setup
Base = declarative_base()
engine = create_engine('sqlite:///mybooks.db')  # Use your existing DB name if you want
Session = sessionmaker(bind=engine)
session = Session()

# 2. Define a model
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year})>"

# 3. Create the table
Base.metadata.create_all(engine)

# 4. Add a new book
new_book = Book(title="Atomic Habits", author="James Clear", year=2018)
session.add(new_book)
session.commit()

# 5. Retrieve all books
books = session.query(Book).all()
print("\nAll books:")
for book in books:
    print(book)

# 6. Modify a book (change title of first book)
if books:
    first_book = books[0]
    first_book.title = "Atomic Habits (Updated)"
    session.commit()
    print(f"\nUpdated book: {first_book}")

# 7. Retrieve again to confirm update
books = session.query(Book).all()
print("\nAll books after update:")
for book in books:
    print(book)

# 8. (Optional) Clean up session
session.close()
