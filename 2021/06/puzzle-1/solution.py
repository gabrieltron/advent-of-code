import heapq
from collections import defaultdict, deque


SIMULATION_DAYS = 256


with open('input.txt', 'r') as input:
    proliferation_days = list(map(int, input.read().split(',')))

proliferation_day_counter = defaultdict(int)
total_fishes = 0
for proliferation_day in proliferation_days:
    proliferation_day_counter[proliferation_day] += 1
    total_fishes += 1

for today in range(SIMULATION_DAYS):
    new_fishes = proliferation_day_counter[today]
    total_fishes += new_fishes
    current_fishes_proliferation_day = today + 6 + 1
    new_fishes_proliferation_day = today + 8 + 1
    proliferation_day_counter[current_fishes_proliferation_day] += new_fishes
    proliferation_day_counter[new_fishes_proliferation_day] += new_fishes

print(total_fishes)
