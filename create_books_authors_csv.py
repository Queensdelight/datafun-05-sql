import csv

# Define the data to be written to the CSV file
data = [
    ["Book Title", "Author", "Genre", "Year Published", "ISBN"],
    ["To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, "978-0061120084"],
    ["1984", "George Orwell", "Dystopian", 1949, "978-0451524935"],
    ["Pride and Prejudice", "Jane Austen", "Romance", 1813, "978-1503290563"],
    ["The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925, "978-0743273565"],
    ["Moby Dick", "Herman Melville", "Adventure", 1851, "978-1503280786"],
    ["War and Peace", "Leo Tolstoy", "Historical", 1869, "978-1400079988"],
    ["The Catcher in the Rye", "J.D. Salinger", "Fiction", 1951, "978-0316769488"],
    ["The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, "978-0547928227"],
    ["Crime and Punishment", "Fyodor Dostoevsky", "Philosophical", 1866, "978-0486415871"],
    ["The Odyssey", "Homer", "Epic", "8th Century BC", "978-0140268867"]
]

# Define the CSV file name
csv_file = "books_authors.csv"

# Write data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_file}' created successfully.")
