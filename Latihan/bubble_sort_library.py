def bubble_sort_books(books):
    n = len(books)
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j]["jumlah_halaman"] > books[j+1]["jumlah_halaman"]:
                books[j], books[j+1] = books[j+1], books[j]

books_list = [
    {"judul": "Harry Potter and the Sorcerer's Stone", "penulis": "J.K. Rowling", "jumlah_halaman": 320},
    {"judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "jumlah_halaman": 281},
    {"judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "jumlah_halaman": 180},
    {"judul": "Pride and Prejudice", "penulis": "Jane Austen", "jumlah_halaman": 432},
    {"judul": "1984", "penulis": "George Orwell", "jumlah_halaman": 328}
]

bubble_sort_books(books_list)
print("Daftar buku yang diurutkan berdasarkan jumlah halaman secara berurut:")
for books in books_list:
    print("Judul:", books["judul"])
    print("Penulis:", books["penulis"])
    print("Jumlah Halaman:", books["jumlah_halaman"])
    print()