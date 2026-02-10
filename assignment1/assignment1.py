"""
Author: Arnaldo Neto
Assignment: #1
"""
# B) 
gym_member = "Arnaldo Neto"        # string
preferred_weight_kg = 75.5         # float
highest_reps = 12                  # int
membership_active = True           # boolean

# c) 
workout_stats = {
    "Arnaldo": (30, 45, 90),    # yoga, running, weightlifting
    "Pedro": (25, 65, 95),
    "Joseane": (45, 32, 35),
}
# D) 
for friend, minutes_tuple in list(workout_stats.items()):
    if isinstance(minutes_tuple, tuple):  
        workout_stats[f"{friend}_Total"] = sum(minutes_tuple)


friends = [name for name, val in workout_stats.items() 
           if isinstance(val, tuple)]

# E)
workout_list = [list(workout_stats[name]) for name in friends]

# F) 
print("\nYoga and Running minutes for all friends:")
for sports, name in enumerate(friends):
    yoga_running = workout_list[sports][0:2]  
    print(f"{name}: Yoga={yoga_running[0]}, Running={yoga_running[1]}")

print("\nWeightlifting minutes for the last two friends:")
last_two = friends[-2:]
for name in last_two:
    row_index = friends.index(name)
    weightlifting = workout_list[row_index][2]
    print(f"{name}: Weightlifting={weightlifting}")

# G) 
print("\nChecking who has total workout minutes >= 120:")
for name in friends:
    total = workout_stats[f"{name}_Total"]
    if total >= 120:
        print(f"Great job staying active, {name}!")

# H)
user_input = input("\nEnter a friend's name (Arnaldo,Pedro,Joseane): ").strip()
user_input = user_input.title()

if user_input in workout_stats and isinstance(workout_stats[user_input], tuple):
    yoga, running, weightlifting = workout_stats[user_input]
    total = workout_stats[f"{user_input}_Total"]

    print(f"\n{user_input}'s workout minutes:")
    print(f"Yoga: {yoga}")
    print(f"Running: {running}")
    print(f"Weightlifting: {weightlifting}")
    print(f"Total: {total}")
else:
    print(f"Friend {user_input} not found in the records.")

# I)
totals = {name: workout_stats[f"{name}_Total"] for name in friends}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"Highest total workout minutes: {highest_friend} ({totals[highest_friend]})")
print(f"Lowest total workout minutes: {lowest_friend} ({totals[lowest_friend]})")
