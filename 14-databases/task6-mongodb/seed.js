db = db.getSiblingDB('library');

db.books.insertMany([
  {
    title: "1984",
    author: { name: "George Orwell", birth_year: 1903 },
    genres: ["dystopian", "political"],
    available: false,
    borrowed_by: {
      user_id: "u001",
      name: "Jonas",
      borrowed_date: "2024-10-01"
    }
  },
  {
    title: "The Wind-Up Bird Chronicle",
    author: { name: "Haruki Murakami", birth_year: 1949 },
    genres: ["fiction", "surreal"],
    available: true
  }
]);