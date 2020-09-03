# Don't change the following lines
import math

number_of_cycles = float(input("Number of cycles: "))
number_of_lines = int(input("Stretched over how many lines? "))

radians_per_line = number_of_cycles * 2 * math.pi / number_of_lines

for line_number in range(0,number_of_lines):
    radians = line_number * radians_per_line
    sin= math.sin(radians)

    if(sin == -1):
        number_of_x = 0
    elif( sin < 0 ):
        number_of_x = round(20 - (abs(sin) * 20))
    elif(sin == 0):
        number_of_x = 20
    elif(sin > 0 and sin < 1):
        number_of_x = round((sin * 20) + 20)
    else:
        number_of_x = 40

    #print(number_of_x)
        
    for i in range(1,number_of_x+1):
        print('X',end='')
    print()