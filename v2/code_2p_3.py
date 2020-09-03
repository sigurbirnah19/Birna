temp_now = int(input("Current temperature (C°): "))
temp_prev = int(input("Previous temperature (C°): "))

RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"

# ... implement control logic and print the appropriate action
if temp_now >= 350:
    result = SHUTDOWN
elif temp_now < 300 and temp_now <= temp_prev:
    result = RAISE
elif temp_now < 300 and temp_now > temp_prev:
    result = KEEP
elif temp_now == 300:
    result = KEEP
elif temp_now > 300 and temp_now >= temp_prev:
    result = LOWER
elif temp_now > 300 and temp_now < temp_prev:
    result = KEEP
    
print(result)