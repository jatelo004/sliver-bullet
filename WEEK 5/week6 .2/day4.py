import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
goal  = 10000

# All at once, no loop needed
deficit = steps - goal
print("Steps vs 10k goal:", deficit)

# Percentage of goal achieved
pct = (steps / goal * 100).round(1)
print("Percent of goal:", pct)

# Boolean mask: which days hit the goal?
hit = steps >= goal
print("Hit goal:", hit)
print("Days hitting goal:", steps[hit])




# 4 weeks of daily steps (28 days)
steps_28 = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])

print(f"28-day step analysis")
print(f"  Mean:        {np.mean(steps_28):,.0f}")
print(f"  Median:      {np.median(steps_28):,.0f}")
print(f"  Std dev:     {np.std(steps_28):,.0f}")
print(f"  Min:         {np.min(steps_28):,}")
print(f"  Max:         {np.max(steps_28):,}")
print(f"  Total:       {np.sum(steps_28):,}")
print(f"  75th pctile: {np.percentile(steps_28, 75):,.0f}")
print(f"  Days 10k+:   {np.sum(steps_28 >= 10000)}/28")


import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("First 3 days:", steps[:3])
print("Last 2 days:", steps[-2:])
print("Weekdays (Mon-Fri):", steps[:5])
print("Weekend:", steps[5:])

print()
# Best week start: first day above 10k
first_10k = np.argmax(steps >= 10000)   # index of first True
print(f"First 10k+ day: {days[first_10k]} with {steps[first_10k]:,} steps")

# Sort and show progression
sorted_steps = np.sort(steps)
print("Steps sorted low to high:", sorted_steps)



import pandas as pd
import numpy as np

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
})

# Pull a column as a NumPy array
steps_arr = df["steps"].to_numpy()
print("NumPy array from pandas column:", steps_arr)
print("Type:", type(steps_arr))

# Use NumPy on it
print(f"\nMean:    {np.mean(steps_arr):,.0f}")
print(f"Std dev: {np.std(steps_arr):,.0f}")

# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df["steps_norm"] = (df["steps"] - df["steps"].min()) / (df["steps"].max() - df["steps"].min())
df["steps_norm"] = df["steps_norm"].round(3)
print("\nWith normalized steps:")
print(df[["day", "steps", "steps_norm"]].to_string())




import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
bench_press_kg = np.array([80, 82, 78, 85, 80, 83, 84])

print("Steps:", steps)
print("Bench press (kg):", bench_press_kg)

# Correlation
corr_matrix = np.corrcoef(steps, bench_press_kg)
print("\nCorrelation matrix:")
print(corr_matrix)

correlation = corr_matrix[0, 1]
print(f"\nCorrelation coefficient: {correlation:.3f}")






import numpy as np

# Maize yield (90kg bags) per plot over a single season
yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

print("MAIZE YIELD ANALYSIS (90kg bags per plot)")
print(f"  Plots:        {len(yields)}")
print(f"  Total yield:  {np.sum(yields)} bags ({np.sum(yields) * 90:,} kg)")
print(f"  Mean:         {np.mean(yields):.1f} bags/plot")
print(f"  Median:       {np.median(yields):.1f} bags/plot")
print(f"  Std dev:      {np.std(yields):.1f}")
print(f"  Best plot:    {np.max(yields)} bags")
print(f"  Worst plot:   {np.min(yields)} bags")
print(f"  Top 25% (75th pctile): {np.percentile(yields, 75):.0f} bags")

print()
# Revenue at KES 2,800 per 90kg bag
revenue = yields * 2800
print("REVENUE (KES 2,800 per bag)")
print(f"  Total:        KES {np.sum(revenue):,}")
print(f"  Avg/plot:     KES {np.mean(revenue):,.0f}")

print()
# Correlation between rainfall and yield
corr = np.corrcoef(rainfall_mm, yields)[0, 1]
print(f"Rainfall vs yield correlation: {corr:.2f}")
print("(1.0 = perfect positive link, 0 = no link)")




import numpy as np

yields = np.array([18, 22, 15, 31, 27, 19, 24, 12, 28, 21, 17, 25])
rainfall_mm = np.array([420, 510, 380, 620, 590, 440, 530, 310, 610, 490, 400, 560])

mean_yield = np.mean(yields)

# High vs low performing plots
high_mask = yields > mean_yield
low_mask = ~high_mask

print("=== HIGH vs LOW PERFORMING PLOTS ===")
print(f"High performers: {np.sum(high_mask)} plots")
print(f"  Avg yield:     {np.mean(yields[high_mask]):.1f} bags")
print(f"  Avg rainfall:  {np.mean(rainfall_mm[high_mask]):.1f} mm")
print(f"  Total bags:    {np.sum(yields[high_mask])}")

print(f"\nLow performers:  {np.sum(low_mask)} plots")
print(f"  Avg yield:     {np.mean(yields[low_mask]):.1f} bags")
print(f"  Avg rainfall:  {np.mean(rainfall_mm[low_mask]):.1f} mm")
print(f"  Total bags:    {np.sum(yields[low_mask])}")

# Bonus: Rank plots by yield
ranked = np.argsort(yields)[::-1]  # descending order
print("\n=== TOP 3 PLOTS ===")
for i, idx in enumerate(ranked[:3], 1):
    print(f"{i}. Plot {idx+1}: {yields[idx]} bags | {rainfall_mm[idx]} mm rain")