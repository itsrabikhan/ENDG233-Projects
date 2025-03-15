# analysis.py
# ENDG 233 F24
# Rabi Khan
# A terminal-based program for analyzing home sales records.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support compound data structures, user entry, printing, or casting (such as len(), input() or int())
# Remember to include comments throughout your code and follow the provided docstring instructions.


# ******************************************************************************************************
# Data is imported from the included records.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any data- all values should be used from records.py.
# An alternate version of records data will be used to test your code.

import records
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE FUNCTIONS HERE
# You must complete and use all of the functions presented below
# Some functions are already fully defined for you.
# If a function continues the word "pass", you should delete "pass" and complete the functions below.
# Use the provided docstring information to determine the exact input/output/behaviour of each function.


def invalid_input():
    """This function prints out a message indicating an invalid input"""
    print(f"\n{'':-^70s}")                                  # Prints a dashed line
    print(f"Error! Invalid input. Please try again.\n")     # Adds a print statement to print the error message.
    
def no_records(region):
    """Prints a message indicating that no records were found for the selected region

    Parameters:
        region (str): a valid region
    """
    print(f"\nThere are no records available for the {region} region.")  # Adds a print statement if no records are found in the dataset for a valid region.

def exit_message():
    """Prints the exit message at the end of the program"""
    print(f"{'':=^70s}")                              # Prints a dashed line
    print(f"\n\nThank you for using our program.")    # Adds a print statement to print the final closing message.
    
    
# COMPLETED FUNCTIONS

def get_region():
    """Prints the prompt to select the region and returns a capitalized valid region name

    Returns:
        user_input (str): a capitalized valid input provided by the user
    """
    
    # Ask until a VALID option is given.
    while True:
        region = input("Enter the region you want to select (e.g. NE) or type '0' to quit: ").upper()
        # If value is a valid region or if value is 0, return the value.
        if region in records.regions or region == '0':
            return region
        else: # If value is invalid, print error and try again, naturally continuing loop.
            invalid_input()


def print_options():
    """Prints the inner menu thats prompts the user to select a data analysis option and returns a valid option number

    Returns:
        int: a valid input provided by the user
    """

    # Ask until a VALID option is given.
    while True:
        print("\nEnter the number of the option you want to select:")
        print("\t1) Print Average Price")
        print("\t2) Print Maximum Bedrooms and Bathrooms")
        print("\t0) Return to Main Menu")
        # Try/except statement to handle casting exceptions.
        try:
            choice = int(input(">> "))
            if choice in range(0, 3): # 0, 1, 2
                return choice
            invalid_input()
        except ValueError:
            # If a ValueError is caught (casting exception), show invalid input and try again (loop will naturally continue).
            invalid_input()


def get_average_price(region):
    """Takes the selected region and returns the average price of homes in the selected region

    Parameters:
        region (str): a valid region

    Returns:
        (if records in that region exist):
            float: the average price of units in the selected region
        (if no records exist):     
            int: a flag value of -1
    """

    # Filter the data so only data for the selected region is included.
    region_data = [record for record in records.data if record[0] == region]
    if len(region_data) == 0: # Return -1 if empty.
        return -1

    # Use list comprehension to create a new list of only prices.
    price_data = [record[1] for record in region_data]

    # Use walrus operator and list comprehension to sum prices to avoid using sum().
    # I recently found out sum() is allowed, but this was fun to learn so I will not change it.
    price_sum = 0
    [price_sum := price_sum + price for price in price_data]
    
    average_price = price_sum / len(price_data)
    return average_price

    
def get_bed_bath_max(region):
    """Takes the selected region and returns the maximum number of rooms and maximum number of bathrooms

    Parameters:
        region (str): a valid region

    Returns:
        (if records in that region exist):
            list: [maximum number of bedrooms, maximum number of bathrooms]
        (if no records exist):     
            int: a flag value of -1
    """
    
    # Filter the data so only data for the selected region is included.
    region_data = [record for record in records.data if record[0] == region]

    if len(region_data) == 0: # Return -1 if empty.
        return -1

    # Create a new list of only integer amounts of bedrooms and bathrooms respectively.
    bedrooms = [int(record[2]) for record in region_data]
    bathrooms = [int(record[3]) for record in region_data]

    return [max(bedrooms), max(bathrooms)]


def print_average_price(region, average_price):
    """Prints the average price of units in a region or calls the no records message

    Parameters:
        region (str): a valid region
        average_price 
            (float): the average price of the units in a region
            (-1): if there are no records
    """

    if average_price == -1:
        no_records(region)
        return
    
    print(f"\nThe average unit price for the {region} region is ${average_price:.2f}")


def print_bed_bath_max(region, data):
    """Prints the maximum bedrooms and bathrooms in a region or calls the no records message

    Parameters:
        region (str): a valid region
        data 
            (list): [maximum number of bedrooms, maximum number of bathrooms]
            (-1): if there are no records
    """

    if data == -1:
        no_records(region)
        return

    # For increased readability.
    maximum_bedrooms = data[0]
    maximum_bathrooms = data[1]
    print(f"\nThe {region} region has a maximum of {maximum_bedrooms} bedrooms and {maximum_bathrooms} bathrooms")


# ******************************************************************************************************
# MAIN PROGRAM DEFINED BELOW

print("ENDG 233 Sales Analysis Program\n")

# While the program is still in use
while True:
    region = get_region()
    if region == "0":
        exit_message()
        break # Exit loop, naturally concluding the program.

    choice = print_options()
    if choice == 1: # average price of region
        average_price = get_average_price(region)
        print_average_price(region, average_price)
    elif choice == 2: # maximum bedrooms and bathrooms
        data = get_bed_bath_max(region)
        print_bed_bath_max(region, data)

    # No else statement is needed, as every case after get_region() is handled.
    # This is because choice = 1 and 2 are handled, and nothing else would satisfy the input function allowing it to continue.
    # The only "neglected" case is 0, which is okay because it leads to the natural conclusion of this iteration.


    # Last line before next initial region prompt
    print(f"{'':=^70s}") # Prints a dashed line
