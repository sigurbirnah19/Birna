#constant declarations
miles_travel_speed_per_hour = 38241
miles_from_sun_base = 16637000000
km_mile = 1.609344
mile_AU = 92955887.6

#calculated helper
miles_travelled_per_day = 24 * miles_travel_speed_per_hour

#request user for day input
days_input = int(input("Number of days after 9/25/09: "))
                        

#calculate distance from input
miles_travelled_for_input_days = miles_travelled_per_day * days_input
miles_accumulated_from_start = miles_from_sun_base + miles_travelled_for_input_days
distance_km = km_mile * miles_accumulated_from_start
distance_astronomical = miles_accumulated_from_start/mile_AU

#print out results
print("Miles from the sun: " + str(miles_accumulated_from_start))
print("Kilometers from the sun: " + str(round(distance_km)))
print ("AU from the sun: " + str(round(distance_astronomical)))
