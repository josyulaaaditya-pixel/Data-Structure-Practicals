lib_data = {
    "M1":["book A", "book B"],
    "M2":[],
    "M3":["book C", "book A"],
    "M4":["book A"],
    "M5":["book B", "book C"],
    "M6":["book A", "book B", "book C", "book D"]

}
total_mem = len(lib_data)
print("Total number of members in the library:", total_mem)

total_borrowed = sum(len(books) for books in lib_data.values())
avg = total_borrowed / total_mem
print("Total number of borrowed books:", total_borrowed)
print("Average number of books borrowed per member:", avg)

all_books = []
for books in lib_data.values():
    all_books.extend(books)
most = max(set(all_books), key=all_books.count)
print("Most borrowed book:", most)  
min_borrowed = min(set(all_books), key=all_books.count)
print("Least borrowed book:", min_borrowed) 
zero = sum(1 for books in lib_data.values() if len(books) == 0)
print("Number of members who have not borrowed any books:", zero)
print("Mode:", most)