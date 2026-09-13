from io import StringIO

milk_log = """Daisy,6.5,7.2
Bella,4.1,4.8
Nala,8.3,9.1
Rosa,3.2,3.5
Lola,7.8,8.4
"""

print("Cow daily totals:")
print("-" * 40)

total_herd_milk = 0
low_producers = []
cow_count = 0

for line in StringIO(milk_log):
    cow, morning, evening = line.strip().split(',')
    morning = float(morning)
    evening = float(evening)
    daily_total = morning + evening
    total_herd_milk += daily_total
    cow_count += 1
    
    flag = ""
    if daily_total < 10:
        flag = "  <-- LOW (below 10 litres)"
        low_producers.append(cow)
    
    print(f"{cow}: {morning} + {evening} = {daily_total:.1f} litres{flag}")

print("\n--- Herd Summary ---")
print(f"Number of cows: {cow_count}")
print(f"Total milk produced: {total_herd_milk:.1f} litres")
print(f"Average per cow: {total_herd_milk / cow_count:.1f} litres")
if low_producers:
    print(f"Cows flagged (below 10 litres): {', '.join(low_producers)}")
else:
    print("No cows flagged.")