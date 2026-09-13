"weekly_report"
def check_steps(steps, goal=8000):
    if steps >= goal:
        print(f"{steps} steps - Goal of {goal} hit.")
    else:
        print(f"{steps} steps - Goal of {goal} missed.")

# Uses the default goal of 8000
check_steps(9200)
check_steps(7500)

# Override the default goal
check_steps(9200, goal=10000)
check_steps(11500, goal=10000)
def log_day(steps, water=8, protocol="OMAD"):
    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")

log_day(9200)                        # Uses both defaults
log_day(10500, water=9)              # Override water only
log_day(8800, water=7, protocol="2MAD")  # Override both
def client_report(name, goal, sessions=4, bench_kg=60):
    print(f"{name} | Goal: {goal} | Sessions/week: {sessions} | Bench: {bench_kg}kg")

# Positional arguments
client_report("James", "fat loss")

# Keyword arguments: order does not matter
client_report(goal="muscle gain", name="Mwangi", bench_kg=100)

# Mix of positional and keyword
client_report("Sandra", "endurance", bench_kg=50)
step_goal = 8000  # Global variable

def check_today(steps):
    result = "hit" if steps >= step_goal else "missed"  # result is local
    print(f"Goal {result}: {steps} steps")

check_today(9200)
check_today(7000)

# This would cause an error - result does not exist here:
# print(result)
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)
category = bmi_category(bmi)

print(f"Weight: {weight}kg | Height: {height}m")
print(f"BMI: {bmi} | Category: {category}")

def weekly_report(name, steps_list, goal=8000):
    days_on_target = 0
    for s in steps_list:
        if s >= goal:
            days_on_target += 1
    avg = sum(steps_list) / len(steps_list)
    print(f"--- {name}'s Week ---")
    print(f"Days tracked : {len(steps_list)}")
    print(f"Days on goal : {days_on_target}")
    print(f"Average steps: {round(avg, 0)}")
    print()

weekly_report("James", [9200, 7500, 10500, 8800, 6900, 11000, 9600])
weekly_report("Sandra", [10000, 10200, 9800, 11000, 10500], goal=10000)
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