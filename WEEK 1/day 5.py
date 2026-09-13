daily_steps=(8200,5100,11300,6800,9400,4200,10100)
target=8000
day=1

for steps in daily_steps:
    print(f"Day:",day,steps,"steps done.")
    if steps>=target:
        print("Target Achieved")
    else:print("Target missed")
    day=day+1

    for steps in daily_steps:
        print(f"Checking :{steps},steps")
        if steps>=target:
            print(f"Target hit on this day:{steps},steps.Stop searching.")
            break
        days=0
        