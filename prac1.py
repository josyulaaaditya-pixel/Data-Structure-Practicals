n = int(input("Enter number of books in the library: "))

library_records = {}

# Take book name and borrow count from user
for i in range(n):
    book_name = input(f"Enter name of book {i+1}: ")
    borrow_count = int(input(f"Enter borrow count for '{book_name}': "))
    library_records[book_name] = borrow_count

# 1. Compute average number of books borrowed
avg_borrowed = sum(library_records.values()) / len(library_records)

# 2. Book with highest and lowest borrowings
highest_book = max(library_records, key=library_records.get)
lowest_book = min(library_records, key=library_records.get)

# 3. Count members who have not borrowed any books
zero_borrow_count = list(library_records.values()).count(0)

# 4. Most frequently borrowed book(s) without using mode()
borrow_counts = list(library_records.values())

# Count frequencies
freq = {}
for count in borrow_counts:
    freq[count] = freq.get(count, 0) + 1

# Find max frequency value
max_freq = max(freq.values())

# Get all borrow counts having this max frequency
most_frequent_counts = [count for count, f in freq.items() if f == max_freq]

# Get all books having one of those counts
most_frequent_books = [book for book, count in library_records.items() if count in most_frequent_counts]

# Display results
print("\n--- Library Borrowing Records Analysis ---")
print(f"Average books borrowed: {avg_borrowed}")
print(f"Book with highest borrowings: {highest_book} ({library_records[highest_book]} times)")
print(f"Book with lowest borrowings: {lowest_book} ({library_records[lowest_book]} times)")
print(f"Number of members with zero borrowings: {zero_borrow_count}")
print(f"Most frequently borrowed book(s): {most_frequent_books} ({most_frequent_counts[0]} times)")
