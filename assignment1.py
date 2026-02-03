#Arnaldo Neto
#assignment1

gym_menber = "Arnaldo Neto"
preferred_weight_kg = 75
highest_reps = 12
membership_active = True


workout_stats = {
    "Arnaldo": (30, 45, 20),    #weightlifting
    "Pedro": (25, 60, 15),      #Running
    "Joseane": (40, 30, 35)     #yoga
}

for friend, minutes_tuple in list(workout_stats.items()):
    if isinstance(minutes_tuple, tuple):  # only calculate totals for tuple entries
        workout_stats[f"{friend}_Total"] = sum(minutes_tuple)

print("Workout stats with totals:")
print(workout_stats)