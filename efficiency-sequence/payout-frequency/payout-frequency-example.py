import sys
import random


num_fetches_in_dog_lifetime = int(sys.argv[1])
minutes_saved_per_successful_fetch = int(sys.argv[2])
probability_of_successful_fetch = float(sys.argv[3])
num_alternate_realities=int(sys.argv[4])

print("total_successes,total_minutes_saved")
for experiment in range(num_alternate_realities):
    total_successes = 0

    for trial in range(num_fetches_in_dog_lifetime):
        if random.random() <= probability_of_successful_fetch:
            total_successes += 1

    total_minutes_saved = total_successes * minutes_saved_per_successful_fetch
    print(f'{total_successes},{total_minutes_saved}')
