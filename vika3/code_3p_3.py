# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
guess = 50
low = 1
high = 100
count = 0
cmd = 's'
# Then start a while loop

while cmd != 'q' and cmd != 'c' and count <7:
    # These lines you can keep as is
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    
    # Now it's up to you to check the command and take appropriate action
    if( cmd == 'l' ):
        low = guess + 1
        guess = (high + low) // 2
    if( cmd == 'h'):
        high = guess - 1
        guess = (high + low) // 2
        
    count = count + 1

if( cmd == 'c' ):
    print('I AM VICTORIOUS')
elif( cmd == 'q' ):
    print('Quitter')    
# If you detect that the user has not been truthful, you should print the following
elif( count >= 7):
    print("Tsk, tsk, don't try to cheat me")
