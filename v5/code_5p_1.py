# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

# Implement the Babylonian square root algorithm
counter = 1
while( abs(guess - prev_guess) > tolerance)
    counter += 1
    

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")
