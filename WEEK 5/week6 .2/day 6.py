# Tiling contractor job records
jobs = [
    {"client": "Kamau", "location": "Kiambu", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "location": "Machakos", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "location": "Kisumu", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "location": "Nakuru", "boxes_used": 60, "price_per_box": 2200},
]

print("Job Summary:")
print("-" * 50)
total_boxes = 0
total_revenue = 0

for j in jobs:
    revenue = j["boxes_used"] * j["price_per_box"]
    print(f"{j['client']} ({j['location']}): {j['boxes_used']} boxes | KES {revenue:,}")
    total_boxes += j["boxes_used"]
    total_revenue += revenue

avg_price = total_revenue / total_boxes

print(f"\nTotal boxes laid: {total_boxes}")
print(f"Total revenue: KES {total_revenue:,}")
print(f"Average price per box: KES {avg_price:.0f}")




jobs = [
    {"client": "Kamau", "location": "Kiambu", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "location": "Machakos", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "location": "Kisumu", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "location": "Nakuru", "boxes_used": 60, "price_per_box": 2200},
    {"client": "Achieng", "location": "Nairobi", "boxes_used": 35, "price_per_box": 1950},
]

print("=== TILING JOBS SUMMARY ===\n")

total_boxes = 0
total_revenue = 0

for job in jobs:
    revenue = job["boxes_used"] * job["price_per_box"]
    print(f"{job['client']:<12} ({job['location']:<10}) → {job['boxes_used']:>3} boxes | KES {revenue:>8,}")
    total_boxes += job["boxes_used"]
    total_revenue += revenue

print("-" * 55)
print(f"{'TOTAL':<12} {'':<12} → {total_boxes:>3} boxes | KES {total_revenue:>8,}")
print(f"\nAverage price per box: KES {total_revenue / total_boxes:,.0f}")

# Bonus: Highest value job
highest = max(jobs, key=lambda j: j["boxes_used"] * j["price_per_box"])
print(f"\nHighest revenue job: {highest['client']} ({highest['location']}) – KES {highest['boxes_used'] * highest['price_per_box']:,}")












herd_data = [
    {"cow": "Daisy", "yields": [72, 68, 74, 70]},
    {"cow": "Bella", "yields": [45, 42, 38, 40]},
    {"cow": "Nala",  "yields": [88, 91, 85, 93]},
    {"cow": "Rosa",  "yields": [55, 58, 52, 50]},
    {"cow": "Lola",  "yields": [78, 80, 76, 82]},
]

results = []

for cow_data in herd_data:
    name = cow_data["cow"]
    yields = cow_data["yields"]
    total = sum(yields)
    average = total / len(yields)
    flagged = average < 60

    results.append({
        "cow": name,
        "total": total,
        "average": average,
        "flagged": flagged
    })

    print(f"{name}: Total = {total} litres, "
          f"Average = {average:.2f} litres/week, "
          f"Flagged = {flagged}")

# Identify top producer
top_producer = max(results, key=lambda x: x["total"])
print(f"\nTop producer: {top_producer['cow']} "
      f"with {top_producer['total']} litres total")

# List flagged cows
flagged_cows = [r["cow"] for r in results if r["flagged"]]
print(f"Cows with average below 60 litres: {flagged_cows}")







