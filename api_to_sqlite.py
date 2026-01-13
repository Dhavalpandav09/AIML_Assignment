import requests
import sqlite3

API_URL = "https://openlibrary.org/search.json?q=python"

response = requests.get(API_URL)
data = response.json()

books = data["docs"]   

# Database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

# Insert
for book in books:
    title = book.get("title", "N/A")
    
    author = "Unknown"
    if "author_name" in book:
        author = ", ".join(book["author_name"])

    year = book.get("first_publish_year", 0)

    cursor.execute("""
    INSERT INTO books (title, author, year)
    VALUES (?, ?, ?)
    """, (title, author, year))

conn.commit()

# Display
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
