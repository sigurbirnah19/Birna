age = int(input("Input age: ")) # Do not change this line

base_cost = 40
cost = 40.0

if age >=65:
    cost = 0.6 * base_cost
elif age < 20 and age > 5:
    cost = 0.8 * base_cost
elif age <= 5:
    cost = 0.0

print(cost)