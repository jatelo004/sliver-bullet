import json

week_report = {
    "name": "Fellex",
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON output:")
print(json_str)

# Load back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")