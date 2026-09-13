import math

total_days = 50
training_days_per_week = 5
weeks = total_days / 7

print(f"Total days: {total_days}")
print(f"Full weeks: {math.floor(weeks)}")

# Distance calculation using Pythagoras
walk_east = 3.0   # km
walk_north = 4.0  # km
distance = math.sqrt(walk_east**2 + walk_north**2)
print(f"Direct distance: {distance} km")
import math

# Square root
print("Square root of 144:", math.sqrt(144))

# Round down and round up
print("Floor of 7.9:", math.floor(7.9))
print("Ceiling of 7.1:", math.ceil(7.1))

# Pi
print("Pi:", math.pi)

# Power: 2 to the power of 10
print("2 to the 10th:", math.pow(2, 10))
import random
import math

total_days = 50
training_days_per_week = 5
weeks = total_days / 7

print(f"Total days: {total_days}")
print(f"Full weeks: {math.floor(weeks)}")

# Distance calculation using Pythagoras
walk_east = 3.0   # km
walk_north = 4.0  # km
distance = math.sqrt(walk_east**2 + walk_north**2)
print(f"Direct distance: {distance} km")
import random
import math

def generate_week():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    total = 0
    goal_days = 0

    for day in days:
        steps = random.randint(6000, 12000)
        total += steps
        if steps >= 8000:
            goal_days += 1
        print(f"  {day}: {steps} steps")

    avg = math.floor(total / 7)
    print(f"\nAverage steps : {avg}")
    print(f"Days on goal  : {goal_days}/7")

generate_week()