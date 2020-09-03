rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below

if rating >= 2700:
    print("Super grandmaster") # Do not change this line
elif 2700 > rating >= 2500:
    print("Grandmaster") # Do not change this line
elif 2500 > rating >= 2400:
    print("International") # Do not change this line
elif 2400 > rating > 999:
    print("Amateur") # Do not change this line
else:
    print("Invalid") # Do not change this line
