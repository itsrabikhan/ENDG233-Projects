# Rabi Khan
# ENDG 233 Fall 2024
# Portfolio Project 1
# race.py
# Program for calculating the time it takes for a car to complete a race depending
# on car parameters, driver recklessness, and road conditions.

import math

# CONSTANTS AND INITIALIZATION

class Car: # Object class for cars.
    def __init__(self, top_speed, fuel_capacity, fuel_efficiency):
        self.top_speed = top_speed # value in km/h
        self.fuel_capacity = fuel_capacity # value in L
        self.fuel_efficiency = fuel_efficiency # value in km/L

# Car constants, with respective units as defined in object constructor.
VEYRON = Car(431, 100, 3.1)
VALKYRIE = Car(402, 90, 6.8)
LAFERRARI = Car(350, 85, 6.4)

# Final time multipliers.
# Note that the driver recklessness multiplier is organized such that
# the driver selection number (subtract 1) is the index in the list below.
DRIVER_RECKLESSNESS_MULTIPLIER = [1.1, 1.2, 1.3] # accounting for recklessness
WET_ROAD_MULTIPLIER = 1.3 # accounting for weather


# INPUT READING

car_selection = int(input("Select a car number: ")) # 1, 2, or 3
driver_selection = int(input("Select a driver number: ")) # 1, 2, or 3
distance = int(input("How long is the race in kilometers?: ")) # any integer

# Input must be handled separately as boolean casting works differently.
is_road_wet = True if input("Is the road going to be wet? (True or False): ").lower() == "true" else False


# INPUT VALIDATION
# For readability and simplification, ranges are used rather than
# greater than or less than comparators. This solution may be less
# efficient in different scenarios, but works fine for this one.

if car_selection in range(1, 4) and driver_selection in range(1, 4):
    # Assign respective car object.
    if car_selection == 1:
        car = VEYRON
    elif car_selection == 2:
        car = VALKYRIE
    elif car_selection == 3:
        car = LAFERRARI
    # no need for else statement, it would be redundant


    # CALCULATIONS
    # These calculations are split up for readability.

    # Range is the distance a car can travel before running out of fuel.
    car_range = car.fuel_efficiency * car.fuel_capacity

    # Refuels is the number of times the car needs to refuel during the race.
    refuels = math.floor(distance / car_range)

    # Refuel time is how long the car ends up taking to refuel during the race.
    refuel_time = (6 / 60) * refuels

    # Race time is the total amount of time taken actually DRIVING.
    race_time = distance / car.top_speed # assumed no acceleration

    # Road multiplier is the final multiplier depending on the road condition.
    road_multiplier = 1
    if is_road_wet:
        road_multiplier = WET_ROAD_MULTIPLIER

    # Total time is the final amount for how long is taken for the race.
    total_time = race_time + refuel_time
    total_time *= DRIVER_RECKLESSNESS_MULTIPLIER[driver_selection - 1]
    total_time *= road_multiplier
    total_time = round(total_time, 1)

    # Final calculated value output.
    print("The total travel time for Car {0} with Driver {1} to travel {2} km is {3:0.1f} hours.".format(car_selection, driver_selection, distance, total_time))
else:
    print("Input number not recognized.")