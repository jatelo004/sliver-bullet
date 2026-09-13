with open("daily_log.txt", "w") as f:
    f.write("Steps: 9200\n")
    f.write("Water: 8 glasses\n")
    f.write("Protocol: OMAD\n")
    f.write("Cold shower: Yes\n")
    import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print("File written. Contents:")
print(file_content.getvalue())
with open("daily_log.txt", "r") as f:
    content = f.read()
    print(content)
    import io

file_data = """Steps: 9200
Water: 8
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
Pages read: 30
"""

log = {}
f = io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":", 1)
        log[key.strip()] = value.strip()

print("Parsed log:")
for key, value in log.items():
    print(f"  {key}: {value}")
    import io

file_data = """Steps: 9200
Water: 8
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
Pages read: 30
"""

log = {}
f = io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":", 1)
        log[key.strip()] = value.strip()

print("Parsed log:")
for key, value in log.items():
    print(f"  {key}: {value}")
    import io

file_data = """Steps: 9200
Water: 8
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
Pages read: 30
"""

log = {}
f = io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":", 1)
        log[key.strip()] = value.strip()

print("Parsed log:")
for key, value in log.items():
    print(f"  {key}: {value}")
    import io

# Start with existing content
file_data = "Steps: 9200\nWater: 8 glasses\nProtocol: OMAD\n"

# Simulate append
file_data += "Pages read: 30\n"
file_data += "Workout: bench press 5x5 at 80kg\n"

print("File after appending:")
print(file_data)
import io

# Simulated file: one line per day with step count
weekly_data = """Monday: 9200
Tuesday: 7500
Wednesday: 10500
Thursday: 8800
Friday: 6900
Saturday: 11000
Sunday: 9600
"""

goal = 8000
days_on_goal = 0

f = io.StringIO(weekly_data)
for line in f:
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split(":", 1)
        steps = int(steps_str.strip())
        status = "Goal hit" if steps >= goal else "Below goal"
        print(f"{day}: {steps} steps - {status}")
        if steps >= goal:
            days_on_goal += 1

print(f"\nDays on goal: {days_on_goal}/7")