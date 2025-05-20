from datetime import datetime, timedelta


class Book:
    def __init__(self, title, author, isbn, published_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_year = published_year
        self.available = True
        
    def __str__(self):
        status = "Tersedia" if self.available else "Dipinjam"
        return f"{self.title} oleh {self.author} ({self.published_year}) - {status}"


class Library:
    location = "Jakarta"
    total_books = 0
    catalog = []
    borrowed_books = {}  
    
    def __init__(self, name):
        self.name = name
        self.founding_date = datetime.now()
    
    def add_book(self, book):
        """Metode instansi untuk menambahkan buku ke perpustakaan"""
        if not isinstance(book, Book):
            raise TypeError("Objek harus dari kelas Book")
        
        Library.catalog.append(book)
        Library.total_books += 1
        print(f"Buku '{book.title}' telah ditambahkan ke perpustakaan {self.name}")
    
    def borrow_book(self, isbn, user_id):
        """Metode instansi untuk peminjaman buku"""
        for book in Library.catalog:
            if book.isbn == isbn and book.available:
                book.available = False
                due_date = datetime.now() + timedelta(days=14)  
                Library.borrowed_books[isbn] = (user_id, due_date)
                print(f"Buku '{book.title}' dipinjam oleh {user_id}")
                print(f"Tanggal pengembalian: {due_date.strftime('%d-%m-%Y')}")
                return True
        print("Buku tidak tersedia untuk dipinjam")
        return False
    
    def return_book(self, isbn):
        """Metode instansi untuk pengembalian buku"""
        if isbn in Library.borrowed_books:
            for book in Library.catalog:
                if book.isbn == isbn:
                    book.available = True
                    borrower, due_date = Library.borrowed_books[isbn]
                    del Library.borrowed_books[isbn]
                    print(f"Buku '{book.title}' telah dikembalikan")
                    return True
        print("Buku ini tidak terdaftar sebagai buku yang dipinjam")
        return False
    
    @classmethod
    def get_available_books(cls):
        """Metode kelas untuk mendapatkan semua buku yang tersedia"""
        available_books = [book for book in cls.catalog if book.available]
        return available_books
    
    @classmethod
    def change_location(cls, new_location):
        """Metode kelas untuk mengubah lokasi perpustakaan"""
        old_location = cls.location
        cls.location = new_location
        print(f"Lokasi perpustakaan diubah dari {old_location} ke {new_location}")
        return True
    
    @classmethod
    def get_borrowed_books_by_user(cls, user_id):
        """Metode kelas untuk mencari buku yang dipinjam oleh pengguna tertentu"""
        user_books = []
        for isbn, (borrower, due_date) in cls.borrowed_books.items():
            if borrower == user_id:
                for book in cls.catalog:
                    if book.isbn == isbn:
                        user_books.append((book, due_date))
        return user_books
    
    @staticmethod
    def is_isbn_valid(isbn):
        """Metode statis untuk memeriksa apakah ISBN valid"""
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        
        sum_digits = 0
        for i, digit in enumerate(isbn[:-1]):
            if i % 2 == 0:
                sum_digits += int(digit)
            else:
                sum_digits += int(digit) * 3
        
        check_digit = (10 - (sum_digits % 10)) % 10
        return check_digit == int(isbn[-1])
    
    @staticmethod
    def calculate_fine(due_date):
        """Metode statis untuk menghitung denda keterlambatan"""
        today = datetime.now()
        if today <= due_date:
            return 0
        
        days_late = (today - due_date).days
        fine_rate = 2000  
        return days_late * fine_rate
    
    @staticmethod
    def format_date(date):
        """Metode statis untuk memformat tanggal"""
        return date.strftime("%d %B %Y")


if __name__ == "__main__":
    central_library = Library("Perpustakaan Pusat")
    branch_library = Library("Perpustakaan Cabang")
    
    book1 = Book("Python Programming", "John Doe", "9780123456789", 2020)
    book2 = Book("Data Science Basics", "Jane Smith", "9781234567890", 2019)
    book3 = Book("Web Development", "Michael Brown", "9782345678901", 2021)
    
    central_library.add_book(book1)
    central_library.add_book(book2)
    branch_library.add_book(book3)
    
    print(f"\nTotal buku di perpustakaan: {Library.total_books}")
    print(f"Lokasi perpustakaan: {Library.location}")
    
    Library.change_location("Bandung")
    print(f"Lokasi baru perpustakaan: {Library.location}")
    
    print("\nMeminjam buku:")
    central_library.borrow_book("9780123456789", "user001")
    
    available_books = Library.get_available_books()
    print("\nBuku yang tersedia:")
    for book in available_books:
        print(f"- {book}")
    
    borrowed_books = Library.get_borrowed_books_by_user("user001")
    print("\nBuku yang dipinjam oleh user001:")
    for book, due_date in borrowed_books:
        print(f"- {book.title}, harus dikembalikan pada: {Library.format_date(due_date)}")
    
    test_isbn = "9780123456789"
    print(f"\nApakah ISBN {test_isbn} valid? {Library.is_isbn_valid(test_isbn)}")
    
    late_date = datetime.now() - timedelta(days=5)
    fine = Library.calculate_fine(late_date)
    print(f"Denda keterlambatan untuk buku yang jatuh tempo 5 hari lalu: Rp{fine}")

    print("\nMengembalikan buku:")
    central_library.return_book("9780123456789")
    
    available_books = Library.get_available_books()
    print("\nBuku yang tersedia setelah pengembalian:")
    for book in available_books:
        print(f"- {book}")