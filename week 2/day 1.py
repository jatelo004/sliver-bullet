week_steps=(8200,5100,11300,6800,9400,4200,10100)
target=8000
for steps in week_steps:
    if steps>=8000:
        print(steps,"-Goal hit")
    else:
        print(steps,"-Below goal ")
        print("Days tracked:",len(week_steps))