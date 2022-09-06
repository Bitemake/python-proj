frequency = "Four times a week"
intensity = "high"
highly_active = frequency == "daily"
print("Higly active user:")
print(highly_active)
high_intensity = intensity == "high"
print("High intensity sports:")
print(high_intensity)
heart_rate = 58
low = heart_rate < 60
high = heart_rate > 100
print("heart rate low:")
print(low)
print("heart rate high:")
print(high)
#a set of exercises and adding 5 kg to the total weight of sports equipment (+5 kg to the weight of dumbbells, barbells, kettlebells)
Maximum_load_capacity_at_the_moment = 25
daily_goal = 5
target = 100
target_hit = Maximum_load_capacity_at_the_moment == target
print("Is the goal fulfilled?")
print(target_hit)
current_daily_goal = Maximum_load_capacity_at_the_moment - daily_goal
in_Maximum_load_capacity_at_the_moment = current_daily_goal !=0
print("Daily goal reached:")
print(in_Maximum_load_capacity_at_the_moment)