# Don't change these lines
number = int(input("Find the square root of integer: "))
guess = int(input("Initial guess: "))
tolerance = float(input("What tolerance: "))

# Implement the Babylonian square root algorithm
count = 0
prev_guess = 0

while( abs(guess - prev_guess) > tolerance):
    count += 1 

    quotient = number / guess

    new_guess = (quotient + guess)/2

    prev_guess = guess
    guess = new_guess

# Don't change these lines
print("Square root of", number, "is", round(guess, 4))
print("Took", count, "reps to get it to tolerance")
