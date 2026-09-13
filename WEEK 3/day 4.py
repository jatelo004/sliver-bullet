weekly_steps=[7800,5000,7656,2456,8754,50006,4765]
goal_days=["steps for steps in weekly_steps if steps=>8000"]
print("goal_days")
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = [steps for steps in weekly_steps if steps >= 8000]

print(goal_days)# Sample data (replace with the actual data you have)
people = ["Alice", "Bob", "Charlie", "Dana"]

weekly_steps = [
    [9200, 7500, 10500, 8800, 6900, 11000, 9600],   # Alice
    [8500, 9200, 11000, 7800, 9500, 10200, 8800],   # Bob
    [11200, 9800, 10500, 9900, 8700, 9400, 10100],  # Charlie
    [7800, 8200, 7600, 9100, 8800, 7900, 8500]     # Dana
]

# (1) All step counts above 10,000 from any person
high_steps = [steps for person in weekly_steps for steps in person if steps > 10000]
print("Steps above 10,000:", high_steps)

# (2) Names of people whose average steps > 9,000
high_avg_people = [
    name for name, steps in zip(people, weekly_steps)
    if sum(steps) / len(steps) > 9000
]
print("People with average > 9,000:", high_avg_people)

