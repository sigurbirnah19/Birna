rating = int(input("Input elo rating: ")) # Do not change this line
# Fill in the missing code below
while rating > 0:
    if(rating > 2700):
        print("Super grandmaster") # Do not change this line
    elif(rating >= 2500):
        print("Grandmaster") # Do not change this line
    elif(rating >=2400):
        print("International") # Do not change this line
    elif(rating < 2400 and rating > 1000):
        print("Amateur") # Do not change this line
    else:
        print("Invalid") # Do not change this line

    rating = int(input("Input elo rating: ")) # Do not change this line
