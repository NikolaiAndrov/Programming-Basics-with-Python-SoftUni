book_pages = int(input())
hour_pages = int(input())
day_count = int(input())
total_time_reading = book_pages // hour_pages
daily_hours_needed = total_time_reading / day_count
print(daily_hours_needed)
