movie = input()
total_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while movie != "Finish":
    capacity = int(input())
    current_ticket_count = 0

    ticket_type = input()
    while ticket_type != "End":
        total_tickets += 1
        current_ticket_count += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if current_ticket_count == capacity:
            break

        ticket_type = input()

    print(f"{movie} - {current_ticket_count / capacity * 100:.2f}% full.")

    movie = input()

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")