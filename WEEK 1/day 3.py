exercises=8
sets_per_exercise=8
reps_per_set=20
weight_per_rep=120
session_duration_minute=90
total_sets=exercises*sets_per_exercise
total_reps=reps_per_set*total_sets
total_volume=total_reps*weight_per_rep
rep_per_minute=total_reps//session_duration_minute
print("===FULL SESSION REPORT===")
print(f"total sets:{total_sets}")
print(f"total reps:{total_reps}")
print(f"total volume:{total_volume}kg")
print(f"reps per minute :{rep_per_minute}")
print(f"reps per minute:{rep_per_minute}")
print( total_volume>1000)
