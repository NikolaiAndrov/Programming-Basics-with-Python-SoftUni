tour_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

toys_count = puzzle_count + doll_count + bear_count + minion_count + truck_count
toys_sum = (puzzle_count * 2.60) + (doll_count * 3) + (bear_count * 4.10) + (minion_count * 8.20) + (truck_count * 2)
toys_sum -= toys_sum * 0.1
if toys_count >= 50:
    toys_sum -= toys_sum * 0.25

if toys_sum >= tour_price:
    final_price = toys_sum - tour_price
    print(f"Yes! {final_price:.2f} lv left.")
elif tour_price > toys_sum:
    final_price = tour_price - toys_sum
    print(f"Not enough money! {final_price:.2f} lv needed.")
