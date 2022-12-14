book = input()
input_line = input()
book_checked = 0
book_is_found = False

while input_line != "No More Books":
    if input_line == book:
        book_is_found = True
        break
    book_checked += 1

    input_line = input()

if book_is_found:
    print(f"You checked {book_checked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_checked} books.")
