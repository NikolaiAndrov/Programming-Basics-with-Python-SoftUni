book = input()
input_line = input()
books_count = 0
book_found = False

while True:
    if input_line == book:
        book_found = True
        break

    if input_line == "No More Books":
        break

    input_line = input()
    books_count += 1

if book_found:
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")