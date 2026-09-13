steps=7500
sleep_hours=6
water_glasses=5
cold_shower=False
pages_read=15
if steps>=10000:
    print("Exellent if steps is above 10000 steps")
elif steps>=7500:
    print("Good.You achieved  7500 steps")
else:print("Needs work otherwise ")
if sleep_hours>=6 and water_glasses>=5 and pages_read>=15:
    print("Sleep hours,water glasses and pages read, is Good")
else:
    print("Sleep hours,water glasses and pages read is low")
if cold_shower:
    print("cold shower completed ")
else:
    print("cold shower skipped ")
print("Great effort,aim higher ,you can do better ")

for day in range(465):
    print("step goal 8000 steps")