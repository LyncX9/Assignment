import json
import os

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year
        }

def load_books_from_json(filename="books.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        try:
            data = json.load(file)
            return [Book(**item) for item in data]
        except json.JSONDecodeError:
            return []

def save_books_to_json(books, filename="books.json"):
    with open(filename, "w") as file:
        json.dump([book.to_dict() for book in books], file, indent=4)

def show_books(books):
    if not books:
        print("Belum ada buku.")
    else:
        print("\nDaftar Buku:")
        for idx, book in enumerate(books, start=1):
            print(f"{idx}. {book.title} oleh {book.author} ({book.year})")


def main():
    books = load_books_from_json()

    while True:
        print("\n=== MANAJEMEN BUKU ===")
        print("1. Tampilkan buku")
        print("2. Tambah buku")
        print("3. Keluar")
        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            show_books(books)

        elif choice == "2":
            title = input("Judul buku: ")
            author = input("Penulis: ")
            year = input("Tahun: ")
            new_book = Book(title, author, year)
            books.append(new_book)  
            save_books_to_json(books)  
            print("Buku berhasil ditambahkan dan disimpan.")

        elif choice == "3":
            print("Keluar.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
