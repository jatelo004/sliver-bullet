steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data:
    try:
        steps = int(item)
        if steps >= 8000:
            print(steps, "- Goal hit")
        else:
            print(steps, "- Below goal")
    except ValueError:
        print(f"'{item}' is not a valid number. Skipping.")

def safe_log_entry(data):
    try:
        steps = int(data["steps"])
    except (ValueError, TypeError, KeyError):
        print("Invalid steps data. Skipping entry.")
        return None

    water    = data.get("water", 0)
    protocol = data.get("protocol", "Unknown")

    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")
    return steps

entries = [
    {"steps": "9200", "water": 8,   "protocol": "OMAD"},
    {"steps": "bad",  "water": 7,   "protocol": "2MAD"},
    {"steps": "8800", "protocol": "OMAD"},
    {"steps": "11000","water": 9},
]

results = [safe_log_entry(e) for e in entries]
valid = [r for r in results if r is not None]
print(f"\nValid entries: {len(valid)}")
        