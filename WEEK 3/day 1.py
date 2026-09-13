"day_report"
def day_report(steps, water, protocol):
    print("--- Daily Report ---")
    print(f"Steps    : {steps}")
    print(f"Water    : {water} glasses")
    print(f"Protocol : {protocol}")
    print()

def hit_goal(steps):
    return steps >= 8000

day_report(9200, 8, "OMAD")
day_report(7500, 6, "2MAD")
day_report(11000, 9, "Autophagy Marathon")

print("Goal hit (9200)?", hit_goal(9200))
print("Goal hit (7500)?", hit_goal(7500))