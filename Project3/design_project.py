# design_project.py
# ENDG 233 F24
# Rabi Khan, Daniel Yang
# GROUP 531
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

# IMPORTS

from user_csv import read_csv, write_csv
import matplotlib.pyplot as plt
import numpy as np


# UTILITY CLASSES

class Colors:
    """
    This class contains ANSI escape codes for text colors and styles.
    """

    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    GRAY = "\u001b[90m"
    RESET = "\u001b[0m"
    BOLD = "\u001b[1m"
    UNDERLINE = "\u001b[4m"

class President:
    """
    This object class represents a President of the United States.
    Each President has a name, service number, party, vice president, start year, and end year.

    The start year is inclusive, while the end year may or may not be inclusive.
    The end year is not possible to tell with the data we have, so it is ambiguous.
    It is calculated simply as the start of the next President's term.
    """

    def __init__(self, name: str, number: int, party: str, vice_president: str, start_year: int, end_year: int) -> None:
        """
        Constructor for the President object.

        Parameters:
            name (str): The name of the President.
            number (int): The number of the President in the order of service.
            party (str): The political party of the President.
            vice_president (str): The Vice President in office with the President.
            start_year (int): The year the President took office.
            end_year (int): The year the next President took office. May be None if the President served until the end of the data.

        Returns:
            None
        """

        self.name = name
        self.number = number
        self.party = party
        self.vice_president = vice_president
        self.start_year = start_year
        self.end_year = end_year


# UTILITY FUNCTIONS

def fprint(*args, end: str = "\n") -> None:
    """
    Print function with built-in color reset for convenience.
    This is to be used instead of the built-in print function because of its automatic color reset.

    Parameters:
        *args (any): Any number of arguments to print, can be any type.

    Returns:
        None
    """

    # Altered print statement to include color reset.
    print(str(*args) + Colors.RESET, end=end)

def clear() -> None:
    """
    Clears the terminal screen using an ANSI escape code.

    Parameters:
        None
    
    Returns:
        None
    """

    # ANSI escape code to clear the screen.
    print("\033[H\033[J", end='')

def pause(newlines: int = 1) -> None:
    """
    Pause the program until the user presses Enter.

    Parameters:
        newlines (int): The number of newlines to print before the prompt. Default is 1.

    Returns:
        None
    """

    # Print newlines and prompt the user to press the enter key.
    fprint(("\n" * newlines) + "Press ENTER to continue.", end="")
    input()

def ask_for_year(data: tuple) -> int:
    """
    Ask the user for a year and return it as an integer.
    This function will keep asking until a valid year is entered.
    This function will also ensure that the year is within the range of available data.

    Parameters:
        data (tuple): A tuple containing the data from the CPI, employment, and Presidents datasets.
    
    Returns:
        int: The year entered by the user.
    """

    minimum_year, maximum_year = get_min_max_years(data)
    while True:
        try:
            fprint(f"{Colors.CYAN}Please enter a year ({Colors.GREEN}{minimum_year} - {maximum_year}{Colors.CYAN}): ", end="")
            year = int(input())
            if minimum_year <= year <= maximum_year:
                return year
            else:
                fprint(f"{Colors.RED}Invalid year. Full data is not available for the given year.")
                pause()
        except ValueError:
            fprint(f"{Colors.RED}Invalid year. Please enter a valid integer.")
            pause()

def get_min_max_years(data: tuple) -> tuple:
    """
    Get the minimum and maximum years for which data is available in all datasets.
    This function reads the data from the files and finds the minimum and maximum years.
    The numbers are inclusive on both ends.

    Parameters:
        data (tuple): A tuple containing the data from the CPI, employment, and Presidents datasets.

    Returns:
        tuple: A tuple containing the minimum and maximum years.
    """

    # Load all datasets.
    cpi_data, employment_data, presidents_data = data

    # Get the minimum and maximum years from each dataset.
    # Convert the years to numpy arrays for efficient comparison and to satisfy assignment requirements.
    cpi_years = np.array([int(row[1]) for row in cpi_data])
    employment_years = np.array([int(row[0]) for row in employment_data])
    presidents_years = np.array([int(row[1]) for row in presidents_data])

    # Find the minimum and maximum years that are present in all datasets. 
    minimums = np.array([np.min(cpi_years), np.min(employment_years), np.min(presidents_years)])
    maximums = np.array([np.max(cpi_years), np.max(employment_years), np.max(presidents_years)])
    minimum_year = np.max(minimums)
    maximum_year = np.min(maximums)
    return minimum_year, maximum_year

def load_data() -> tuple:
    """
    Load data from the CSV files and return it as a tuple.
    This function reads the data from the files and returns it as a tuple of lists.

    NOTE: Regarding the Presidents dataset, it is below the minimum requirements for the project.
    The dataset contains less than 50 rows, but this was settled with the course coordinator and an exception was made.

    Parameters:
        None
    
    Returns:
        tuple: A tuple containing the data from the CPI, employment, and Presidents datasets respectively.
    """

    # Read the data from the CSV files. 
    cpi_data = read_csv('data_files/cpi.csv', False)
    employment_data = read_csv('data_files/employment.csv', False)
    presidents_data = read_csv('data_files/presidents.csv', False)

    return cpi_data, employment_data, presidents_data

def get_party_color(party: str) -> str:
    """
    Return the ANSI escape code for the color of the given political party.
    Due to the amount of parties in the dataset, only the two major parties are assigned colors.

    Parameters:
        party (str): The name of the political party.

    Returns:
        str: The ANSI escape code for the assigned party color.
    """

    if "democrat" in party.lower():
        return Colors.BLUE
    elif "republican" in party.lower():
        return Colors.RED
    else:
        return Colors.YELLOW

def get_comparison_colors(value1: float, value2: float, inverted: bool = False) -> list:
    """
    Get the ANSI escape codes for the colors of the two values being compared.
    The colors are determined based on the comparison of the two values.

    By default, lesser values are colored green and greater values are colored red.
    This can be inverted by setting the inverted parameter to True.

    Parameters:
        value1 (float): The first value to compare.
        value2 (float): The second value to compare.
        inverted (bool): Whether to switch the colors. Default is False.

    Returns:
        list: A list containing the ANSI escape codes for the colors of the two values.
    """

    if value1 < value2:
        result = [Colors.GREEN, Colors.RED]
    elif value1 > value2:
        result = [Colors.RED, Colors.GREEN]
    else:
        result = [Colors.YELLOW, Colors.YELLOW]
    
    return [result[1], result[0]] if inverted else result

def save_visualization(path: str, figure: plt.Figure) -> None:
    """ 
    Prompt the user to save visualization. 

    Parameters:
        path (str): A string that gives the path location to the saved graph.
        figure (Figure): The pyplot figure to be saved.

    Returns:
        None
    """

    fprint(f"\n{Colors.GREEN}Would you like to save the visualization? (y/n): {Colors.RESET}", end="")
    option = input().strip().lower()
    if option in ['y', 'yes']:
        figure.savefig(path)
        fprint(f"{Colors.GREEN}Visualization saved succesfully at {Colors.RESET}{path}{Colors.GREEN}.")


# DATA ANALYSIS FUNCTIONS

def calculate_yoy_inflation(data: tuple, year: int, year2: int = None) -> float:
    """
    Calculate the year-over-year inflation rate for a given year.
    This is done by subtracting the CPI at the beginning of the year from the CPI at the end of the year,
    dividing by the CPI at the beginning of the year, and multiplying by 100 to get a percentage.
    If year2 is provided, the rate will be calculated between the two years.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
        year (int): The year for which to calculate the inflation rate.
        year2 (int): The second year for which to calculate the inflation rate. If provided, the rate will be calculated between the two years.
    
    Returns:
        float: The year-over-year inflation rate for the given year (range).
    """

    # From the data tuple, get the CPI data.
    cpi_data = np.array(data[0])

    # If year2 is not provided, filter the data by year.
    # If year2 is provided, filter the data by the range of years.
    if year2 is None:
        year_data = [row for row in cpi_data if row[1] == year]
    else:
        year_data = [row for row in cpi_data if year <= row[1] <= year2]

    # Sort the data primarily by year, then by month using lambda function.
    # This will ensure that the data is sorted correctly in ascending chronological order.
    year_data.sort(key=lambda x: (x[1], x[0]))

    # Get the CPI values for the first and last months of the year.
    # Ideally, this would be January and December respectively, but in case of missing data, it is the first and last months available.
    # If year2 is provided, the CPI values will be taken from the first month of year and the last month of year2.
    start_cpi = year_data[0][2]
    end_cpi = year_data[-1][2]

    # Calculate the year-over-year inflation rate for the year.
    yoy = ((end_cpi - start_cpi) / start_cpi) * 100
    return yoy

def get_president(data: tuple, year: int) -> President:
    """
    Get the name of the President of the United States for a given year.
    Since this information only contains start year, it is possible for multiple presidents to serve in the same year.
    In this case, it will return the name of the last President who served in that year.
    This decision was made because for the most part, Presidents that had a term less than 1 year long did not have a significant enough impact on the economy.
    
    Parameters:
        data (tuple): A tuple containing all of the loaded data.
        year (int): The year for which to get the President.

    Returns:
        President: The President of the United States for the given year. See the President class for more information.
    """

    # From the data tuple, get the Presidents data.
    presidents_data = data[2]

    # Filter only data that is before or equal to the given year.
    # This is done because we are only given start years.
    filtered_data = [row for row in presidents_data if row[1] <= year]

    # If there is no data for the given year, return None.
    if len(filtered_data) == 0:
        return None

    # Sort the data by service number (ascending) using lambda function.
    # Service number is used instead of year because it is more reliable.
    # This is redundant, but is done to ensure that the data is sorted correctly.
    filtered_data.sort(key=lambda x: x[1])

    # Select the most recent President that served in the given year.
    president_data = filtered_data[-1]

    # Get the data for the President.
    name = president_data[2]
    number = int(president_data[0])
    party = president_data[3]
    vice_president = president_data[4]
    start_year = int(president_data[1])

    # Calculate end year by finding the next President's start year.
    # If there is no next President, the President served until the end of the data.
    end_year = None
    index = presidents_data.index(president_data)
    if index < len(presidents_data) - 1:
        end_year = int(presidents_data[index + 1][1])

    # Create a President object and return it.
    president = President(name, number, party, vice_president, start_year, end_year)
    return president

def get_party_years(data: tuple, party: str) -> list:
    """
    Get a list containing all years in which a President of the given party served.
    This function is clamped to the data available in the dataset.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
        party (str): The political party for which to get the years.

    Returns:
        list: A list containing all years in which a President of the given party served.
    """

    # From the data tuple, get the Presidents data.
    presidents_data = data[2]

    # Filter the data by the given party.
    minimum_year, maximum_year = get_min_max_years(data)
    party_data = [row for row in presidents_data if party.lower() in row[3].lower() and minimum_year <= int(row[1]) <= maximum_year]

    # Get the years for the Presidents of the given party.
    party_years = []
    for row in party_data:
        start_year = int(row[1])
        president = get_president(data, start_year)
        party_years.extend(range(president.start_year, president.end_year))

    return party_years

def calculate_employment_rate(data: tuple, year: int) -> float:
    """
    Calculate the employment rate for a given year.
    The employment rate is calculated as the percentage of employed people in the civilian non-institutional population over the age of 16.
    It is important to note that this percentage is not equal to 100% - unemployment rate.
    Another important consideration is that individuals who are not in the labor force are not included in this calculation.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
        year (int): The year for which to calculate the employment rate.

    Returns:
        float: The employment rate for the given year.
    """

    # From the data tuple, get the employment data.
    employment_data = np.array(data[1])

    # Filter the data by year.
    # We take the first row because there should only be one row for each year.
    year_data = [row for row in employment_data if row[0] == year][0]

    # Get the number of employed people and the total civilian non-institutionalized population over the age of 16 for the year.
    employed = year_data[3]
    population = year_data[1]

    # Calculate the employment rate for the year.
    rate = (employed / population) * 100
    return rate

def calculate_unemployment_rate(data: tuple, year: int) -> float:
    """
    Calculate the unemployment rate for a given year.
    The unemployment rate is calculated as the percentage of unemployed people in the civilian labor force.
    It is important to note that this percentage is not equal to 100% - employment rate.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
        year (int): The year for which to calculate the unemployment rate.

    Returns:
        float: The unemployment rate for the given year.
    """

    # From the data tuple, get the employment data.
    employment_data = np.array(data[1])

    # Filter the data by year.
    # We take the first row because there should only be one row for each year.
    year_data = [row for row in employment_data if row[0] == year][0]

    # Get the number of unemployed people and the total labor force for the year.
    unemployed = year_data[4]
    labor_force = year_data[2]

    # Calculate the unemployment rate for the year.
    rate = (unemployed / labor_force) * 100
    return rate

def get_cpi(data: tuple, year: int, month: int) -> float:
    """
    Get the Consumer Price Index (CPI) for a given year and month.

    Parameters:
        year (int): The year for which to get the CPI.
        month (int): The month of that year for which to get the CPI.

    Returns:
        float: The Consumer Price Index for the given year and month.
    """
    
    # From the data tuple, get the CPI data.
    cpi_data = np.array(data[0])

    # Filter the data by year and month.
    # We use the first row because there should only be one row for each year and month.
    cpi = [row for row in cpi_data if row[1] == year and row[0] == month][0][2]
    return cpi

def calculate_inflation_extrema(data: tuple) -> tuple:
    """
    Calculate the years with the highest and lowest inflation rates.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        tuple: A tuple containing the years with the lowest and highest inflation rates respectively.
    """

    # Ensure that data is from the same range.
    minimum_year, maximum_year = get_min_max_years(data)
    years = range(minimum_year, maximum_year + 1)

    # Calculate the inflation rates for each year.
    inflation_rates = np.array([[year, calculate_yoy_inflation(data, year)] for year in years])

    # Find the year with the highest and lowest inflation rates.
    # We use np.argmax and np.argmin to find the indices of the maximum and minimum values.
    minimum_year = int(inflation_rates[np.argmin(inflation_rates[:, 1])][0])
    maximum_year = int(inflation_rates[np.argmax(inflation_rates[:, 1])][0])
    return minimum_year, maximum_year

def calculate_unemployment_extrema(data: tuple) -> tuple:
    """
    Calculate the years with the highest and lowest unemployment rates.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        tuple: A tuple containing the years with the lowest and highest unemployment rates respectively.
    """

    # Ensure that data is from the same range.
    minimum_year, maximum_year = get_min_max_years(data)
    years = range(minimum_year, maximum_year + 1)

    # Calculate the unemployment rates for each year.
    unemployment_rates = np.array([[year, calculate_unemployment_rate(data, year)] for year in years])

    # Find the year with the highest and lowest unemployment rates.
    # We use np.argmax and np.argmin to find the indices of the maximum and minimum values.
    minimum_year = int(unemployment_rates[np.argmin(unemployment_rates[:, 1])][0])
    maximum_year = int(unemployment_rates[np.argmax(unemployment_rates[:, 1])][0])
    return minimum_year, maximum_year

def calculate_employment_extrema(data: tuple) -> tuple:
    """
    Calculate the years with the highest and lowest employment rates.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        tuple: A tuple containing the years with the lowest and highest employment rates respectively.
    """

    # Ensure that data is from the same range.
    minimum_year, maximum_year = get_min_max_years(data)
    years = range(minimum_year, maximum_year + 1)

    # Calculate the employment rates for each year.
    employment_rates = np.array([[year, calculate_employment_rate(data, year)] for year in years])

    # Find the year with the highest and lowest employment rates.
    # We use np.argmax and np.argmin to find the indices of the maximum and minimum values.
    minimum_year = int(employment_rates[np.argmin(employment_rates[:, 1])][0])
    maximum_year = int(employment_rates[np.argmax(employment_rates[:, 1])][0])
    return minimum_year, maximum_year


# MENU FUNCTIONS

def print_title() -> None:
    """
    Read the title from the file and print it in red.

    Parameters:
        None

    Returns:
        None
    """

    clear()
    # Ensuring that the title is read from the file.
    # UTF-8 encoding is used to ensure that the file is read correctly.
    # This is interesting, because removing it only causes problems on Windows.
    with open('title.txt', 'r', encoding='utf-8') as file:
        title = file.read()
        fprint(Colors.RED + title)

def main_menu(data: tuple) -> None:
    """
    Print the main menu of the program.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
    
    Returns:
        None
    """

    # Loop for persistent menu.
    while True:
        # Print the menu.
        print_title()
        fprint(Colors.BOLD + "MAIN MENU\n")
        fprint("1. View Data")
        fprint("2. Compare Data")
        fprint("3. Export CSV")
        fprint("0. Exit")

        # Handle selection cases. 
        option = input(Colors.GREEN + "\n> " + Colors.RESET).strip()
        match option:
            case "1":
                raw_data_menu(data)
                break
            case "2":
                comparison_menu(data)
                break
            case "3":
                export_csv_menu(data)
                break
            case "0":
                goodbye()
                break
            case _:
                fprint(Colors.RED + "Invalid option. Please try again.")
                pause()

def raw_data_menu(data: tuple) -> None:
    """
    Opens the raw data mode menu.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
    
    Returns:
        None
    """

    # Loop for persistent menu.
    while True:
        # Print the menu.
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE\n")
        fprint("1. Select a Year")
        fprint("2. Select a Range of Years")
        fprint("3. Select Political Party")
        fprint("4. View Extrema")
        fprint("0. Back to Main Menu")

        # Handle selection cases. 
        option = input(Colors.GREEN + "\n> " + Colors.RESET).strip()
        match option:
            case "1":
                view_by_year_menu(data)
            case "2":
                view_by_range_menu(data)
            case "3":
                view_by_party_menu(data)
            case "4":
                view_extrema_menu(data)
            case "0":
                main_menu(data)
                break
            case _:
                fprint(Colors.RED + "Invalid option. Please try again.")
                pause()

def view_by_year_menu(data: tuple) -> None:
    """
    View data for a specific year.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.
    
    Returns:
        None
    """

    print_title()
    fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE -> SELECT A YEAR\n")

    # Get the year from the user. 
    year = ask_for_year(data)

    # Get the data for the given year. 
    inflation = calculate_yoy_inflation(data, year)
    employment = calculate_employment_rate(data, year)
    unemployment = calculate_unemployment_rate(data, year)
    president = get_president(data, year)

    # Print the data for the given year.
    fprint(f"\n{Colors.CYAN}Year: {Colors.RESET}{year}")
    fprint(f"{Colors.CYAN}President in Office: {Colors.RESET}{president.name}")
    fprint(f"{Colors.CYAN}Party in Office: {Colors.RESET}{president.party}")
    fprint(f"{Colors.CYAN}Year-over-Year Inflation Rate: {Colors.RESET}{inflation:.2f}%")
    fprint(f"{Colors.CYAN}Employment Rate: {Colors.RESET}{employment:.2f}%")
    fprint(f"{Colors.CYAN}Unemployment Rate: {Colors.RESET}{unemployment:.2f}%")

    # Ask the user if they would like to see a visualization of the data. 
    fprint(f"\n{Colors.GREEN}Would you like to see a visualization of CPI throughout the year? (y/n): {Colors.RESET}", end="")
    option = input().strip().lower()
    if option in ["y", "yes"]:
        inflation_data = [get_cpi(data, year, month) for month in range(1, 13)]

        # Basic plotting.
        figure = plt.figure(figsize=(12, 6))
        plt.plot(range(1, 13), inflation_data)
        plt.title(f"CPI Throughout {year}")
        plt.xlabel("Month")
        plt.ylabel("CPI")
        # Set the x-ticks to be the months. 
        plt.xticks(range(1, 13))
        plt.show()

        # Prompt the user to save the visualization. 
        save_visualization(f"./saved_graphs/{year}_cpi_overview.png", figure)

    pause()

def view_by_range_menu(data: tuple) -> None:
    """ 
    View data for a range of years.
    Keep in mind that a large range of years may result in a large amount of data being displayed.
    This may cause some strange looking graphs.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        None
    """

    # Loop for persistent menu.
    while True:
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE -> SELECT A RANGE OF YEARS")
        fprint("Please keep in mind that a large range of years may result in messy graphs.\n")

        # Get the years from the user. 
        year1 = ask_for_year(data)
        year2 = ask_for_year(data)
        years = range(year1, year2 + 1)

        # Check if the years are the same.
        if year1 == year2:
            fprint(Colors.RED + "You must select two different years. Please try again.")
            pause()
            continue
        
        # Check if the years are in the correct order. 
        if year1 > year2:
            # If order is invalid, simply switch the variables.
            # Create a temporary variable to hold the first value.
            temp = year1
            year1 = year2
            year2 = temp
            # Delete the temporary variable.
            del temp
            # Reassign years variable.
            years = range(year1, year2 + 1)

        # Get the data for the given years. 
        inflation = calculate_yoy_inflation(data, year1, year2)
        change_in_employment = calculate_employment_rate(data, year2) - calculate_employment_rate(data, year1)
        change_in_unemployment = calculate_unemployment_rate(data, year2) - calculate_unemployment_rate(data, year1)

        # Get the most common party for the given years. 
        parties = {
            "Democratic": 0,
            "Republican": 0
        }
        for year in years:
            president = get_president(data, year)
            parties[president.party] += 1
        # Get the party with the most occurrences in the list.
        # Using max with the key parameter alllows us to get the key with the maximum value.
        majority_party = max(parties, key=parties.get)
        majority_party_percentage = (parties[majority_party] / (year2 - year1 + 1)) * 100

        # Clean up and print title. 
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE -> SELECT A RANGE OF YEARS\n")

        # Print the data for the given years. 
        fprint(f"{Colors.CYAN}Years: {Colors.RESET}{year1} - {year2}")
        fprint(f"{Colors.CYAN}Most Common Party: {Colors.RESET}{majority_party} ({majority_party_percentage:.1f}%)")
        fprint(f"{Colors.CYAN}Overall Inflation Rate: {Colors.RESET}{inflation:.2f}%")
        fprint(f"{Colors.CYAN}Change in Employment Rate: {Colors.RESET}{change_in_employment:.2f}%")
        fprint(f"{Colors.CYAN}Change in Unemployment Rate: {Colors.RESET}{change_in_unemployment:.2f}%")

        # Ask the user if they would like to see a visualization of the data.
        fprint(f"\n{Colors.GREEN}Would you like to see a visualization of the data? (y/n): {Colors.RESET}", end="")
        option = input().strip().lower()
        if option in ["y", "yes"]:
            # Create figure, subplots are created after. 
            figure = plt.figure(figsize=(8, 6))

            # Create subplot for monthly CPI data for the years. 
            graph1 = plt.subplot(2, 3, (1, 3))
            graph1.set_title("Monthly CPI Data")
            # Plot the CPI data for each year per month. 
            months = []
            all_months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
            ]
            for year in years:
                months.extend([f"{all_months[i][:3]} {year}" for i in range(12)])
            graph1.plot(months, [get_cpi(data, year, month) for year in years for month in range(1, 13)])
            graph1.set_xlabel("Month")
            graph1.set_xticks(months)
            graph1.set_xticklabels(months, rotation=90)
            graph1.set_ylabel("CPI")

            # Create subplot for inflation rates for the years. 
            graph2 = plt.subplot(2, 3, 4)
            graph2.set_title("Inflation Rates")
            graph2.plot(years, [calculate_yoy_inflation(data, year) for year in years])
            graph2.set_xticks(years)
            graph2.set_xlabel("Year")
            graph2.set_ylabel("Rate (%)")

            # Create subplot for employment rates for the years.
            graph3 = plt.subplot(2, 3, 5)
            graph3.set_title("Employment Rates")
            graph3.plot(years, [calculate_employment_rate(data, year) for year in years])
            graph3.set_xticks(years)
            graph3.set_xlabel("Year")
            graph3.set_ylabel("Rate (%)")

            # Create subplot for unemployment rates for the years.
            graph4 = plt.subplot(2, 3, 6)
            graph4.set_title("Unemployment Rates")
            graph4.plot(years, [calculate_unemployment_rate(data, year) for year in years])
            graph4.set_xticks(years)
            graph4.set_xlabel("Year")
            graph4.set_ylabel("Rate (%)")

            # Adjust layout and show the figure.
            plt.tight_layout()
            plt.show()

            # Prompt the user to save the visualization.
            save_visualization(f"./saved_graphs/{year1}_{year2}_range.png", figure)

        pause()
        break

def view_by_party_menu(data: tuple) -> None:
    """ 
    View data for a specific political party. This menu shows all the years and some calculated data for those years.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        None
    """

    print_title()
    fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE -> SELECT POLITICAL PARTY")

    party = None
    while party is None:
        fprint(f"\n{Colors.GREEN}Please enter the name of the political party: {Colors.RESET}", end="")
        user_party = input().strip().lower()
        # Only these two are necessary as the dataset only contains data for these two parties starting from 1953.
        # 1953 was used as the lower bound because it is the first year available in all 3 datasets.
        if user_party in ["d", "democratic", "demo", "democrat"]:
            party = "Democratic"
        elif user_party in ["r", "republican", "rep", "repub"]:
            party = "Republican"
        else:
            fprint(f"{Colors.RED}Invalid party name. Please try again.")

    # Filter the data by the given party. 
    party_years = get_party_years(data, party)

    # Initialize the table with the column headers. 
    table = [
        [
            f"Year",
            f"President in Office",
            f"Inflation Rate",
            f"Employment Rate",
            f"Unemployment Rate"
        ]
    ]

    # Add data to the table. 
    for year in party_years:
        inflation = calculate_yoy_inflation(data, year)
        employment = calculate_employment_rate(data, year)
        unemployment = calculate_unemployment_rate(data, year)
        president = get_president(data, year)
        table.append([year, president.name, f"{inflation:.2f}%", f"{employment:.2f}%", f"{unemployment:.2f}%"])

    # Finally, print the table with string formatting. 
    print_title()
    fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE -> SELECT POLITICAL PARTY\n")
    party_color = get_party_color(party)
    fprint(f"Party: {party_color}{party}\n")
    for i, row in enumerate(table):
        # Colorize the row headers. 
        # This is done separately to ensure that the color does not affect the alignment. 
        color = Colors.RESET
        if i == 0:
            color = Colors.CYAN + Colors.BOLD
        fprint(f"{color}{str(row[0]):<10} {str(row[1]):<30} {str(row[2]):<20} {str(row[3]):<20} {str(row[4]):<20}")

    pause()

def view_extrema_menu(data: tuple) -> None:
    """ 
    Opens the extrema menu. 
    This menu allows the user to view the years with the highest and lowest values for each of the data points.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        None
    """

    # Print the title and section title.
    print_title()
    fprint(Colors.BOLD + "MAIN MENU -> RAW DATA MODE -> VIEW EXTREMA\n")

    # Calculate the years with the highest and lowest values for each data point. 
    minimum_inflation_year, maximum_inflation_year = calculate_inflation_extrema(data)
    minimum_unemployment_year, maximum_unemployment_year = calculate_unemployment_extrema(data)
    minimum_employment_year, maximum_employment_year = calculate_employment_extrema(data)

    # Create the data table. 
    table = [
        [
            "Data Point", 
            "Minimum Year",
            "Minimum Value",
            "Maximum Year",
            "Maximum Value"
        ],
        [
            "Inflation Rate",
            f"{minimum_inflation_year}",
            f"{calculate_yoy_inflation(data, minimum_inflation_year):.2f}%",
            f"{maximum_inflation_year}",
            f"{calculate_yoy_inflation(data, maximum_inflation_year):.2f}%"
        ],
        [
            "Unemployment Rate",
            f"{minimum_unemployment_year}",
            f"{calculate_unemployment_rate(data, minimum_unemployment_year):.2f}%",
            f"{maximum_unemployment_year}",
            f"{calculate_unemployment_rate(data, maximum_unemployment_year):.2f}%"
        ],
        [
            "Employment Rate",
            f"{minimum_employment_year}",
            f"{calculate_employment_rate(data, minimum_employment_year):.2f}%",
            f"{maximum_employment_year}",
            f"{calculate_employment_rate(data, maximum_employment_year):.2f}%"
        ]
    ]

    # Print the table with string formatting. 
    for i, row in enumerate(table):
        # Colorize the row headers. 
        # This is done separately to ensure that the color does not affect the alignment.
        color = Colors.RESET
        if i == 0:
            color = Colors.CYAN + Colors.BOLD
        fprint(f"{color}{str(row[0]):<20} | {str(row[1]):<20} {str(row[2]):<20} | {str(row[3]):<20} {str(row[4]):<20}")

    pause()
    
def comparison_menu(data) -> None:
    """ 
    Opens the comparison menu.

    Parameters:
        None

    Returns:
        None
    """

    # Loop for persistent menu. 
    while True:
        # Print the menu. 
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> COMPARISON MODE\n")
        fprint("1. Compare Presidents")
        fprint("2. Compare Years")
        fprint("0. Back to Main Menu")

        # Handle selection cases. 
        option = input(Colors.GREEN + "\n> " + Colors.RESET).strip()
        match option:
            case "1":
                compare_presidents_menu(data)
            case "2":
                compare_years_menu(data)
            case "0":
                main_menu(data)
                break
            case _:
                fprint(Colors.RED + "Invalid option. Please try again.")
                pause()

def compare_presidents_menu(data: tuple) -> None:
    """
    Opens the compare presidents menu.
    In this menu, the user can compare two Presidents by inputting a year in which they served.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        None
    """

    # Loop for persistent menu. 
    while True:
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> COMPARISON MODE -> COMPARE PRESIDENTS")
        fprint("Unfortunately, due to some limitations, you may only use years to compare Presidents.")
        fprint("Please enter any year in which the Presidents served to compare them.")

        # Get the Presidents for the given years.
        president1 = None
        while president1 is None:
            print()
            year1 = ask_for_year(data)
            president1 = get_president(data, year1)
            if president1 is None:
                fprint(Colors.RED + "No data available for the given year. Please try again.")
                pause()
            else:
                fprint(f"{Colors.GREEN}Selected: {Colors.RESET}{president1.name}.")

        president2 = None
        while president2 is None:
            print()
            year2 = ask_for_year(data)
            president2 = get_president(data, year2)
            if president2 is None:
                fprint(Colors.RED + "No data available for the given year. Please try again.")
                pause()
            else:
                fprint(f"{Colors.GREEN}Selected: {Colors.RESET}{president2.name}.")

        # Check if the Presidents are the same. 
        if president1.number == president2.number:
            fprint(Colors.RED + "The same President cannot be compared to themselves. Please try again.")
            pause()
            continue

        # Initialize the table with the row headers.
        table = [
            [f"{Colors.CYAN}President"],
            [f"{Colors.CYAN}Party"],
            [f"{Colors.CYAN}Vice President"],
            [f"{Colors.CYAN}Presidential Term"],
            [f"{Colors.CYAN}Years Served"],
            [f"{Colors.CYAN}Inflation Throughout Term"],
            [f"{Colors.CYAN}Average Unemployment Rate"]
        ]
    
        # Before continuing, it is important to note that the case of President.end_year = None is not handled.
        # This will actually never happen in this case, as the data is only available up to 2020.

        # Get colors for the parties. 
        president1_color = get_party_color(president1.party)
        president2_color = get_party_color(president2.party)

        # Add data to the table. 
        table[0].append(president1_color + president1.name)
        table[0].append(president2_color + president2.name)

        # Colorize the party names.
        table[1].append(president1_color + president1.party)
        table[1].append(president2_color + president2.party)

        table[2].append(president1_color + president1.vice_president)
        table[2].append(president2_color + president2.vice_president)

        # Colorize the Presidential terms. 
        # End year case of None is not handled, as it will never happen in this case.
        table[3].append(f"{Colors.MAGENTA}{president1.start_year} - {president1.end_year}")
        table[3].append(f"{Colors.MAGENTA}{president2.start_year} - {president2.end_year}")

        # Calculate term length for each President. 
        president1_term_length = president1.end_year - president1.start_year
        president2_term_length = president2.end_year - president2.start_year

        # Colorize and add the term lengths to the table. 
        term_colors = get_comparison_colors(president1_term_length, president2_term_length, True)
        table[4].append(f"{term_colors[0]}{president1_term_length} years")
        table[4].append(f"{term_colors[1]}{president2_term_length} years")

        # Calculate the inflation rate from the start to end year for each President. 
        president1_inflation = calculate_yoy_inflation(data, president1.start_year, president1.end_year)
        president2_inflation = calculate_yoy_inflation(data, president2.start_year, president2.end_year)

        # Colorize and add the inflation rates to the table. 
        inflation_colors = get_comparison_colors(president1_inflation, president2_inflation)
        table[5].append(f"{inflation_colors[0]}{president1_inflation:.2f}%")
        table[5].append(f"{inflation_colors[1]}{president2_inflation:.2f}%")

        # Get minimum and maximum years to ensure that only available data is used. 
        minimum_year, maximum_year = get_min_max_years(data)

        # Calculate the average unemployment rate for each President. 
        president1_unemployment_total = 0
        for year in range(president1.start_year, president1.end_year + 1):
            if minimum_year <= year <= maximum_year:
                president1_unemployment_total += calculate_unemployment_rate(data, year)
        
        president2_unemployment_total = 0
        for year in range(president2.start_year, president2.end_year + 1):
            if minimum_year <= year <= maximum_year:
                president2_unemployment_total += calculate_unemployment_rate(data, year)

        president1_avg_unemployment = president1_unemployment_total / (president1.end_year - president1.start_year)
        president2_avg_unemployment = president2_unemployment_total / (president2.end_year - president2.start_year)

        # Colorize and add the average unemployment rates to the table.
        unemployment_colors = get_comparison_colors(president1_avg_unemployment, president2_avg_unemployment)
        table[6].append(f"{unemployment_colors[0]}{president1_avg_unemployment:.2f}%")
        table[6].append(f"{unemployment_colors[1]}{president2_avg_unemployment:.2f}%")
        
        # Finally, print the table with string formatting.
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> COMPARISON MODE -> COMPARE PRESIDENTS")
        for row in table:
            fprint(f"{str(row[0]):<40} {str(row[1]):<30} {str(row[2]):<30}")

        # Ask the user if they would like to see a visualization of the data.
        fprint(f"\n{Colors.GREEN}Would you like to see a visualization of the data? (y/n): {Colors.RESET}", end="")
        option = input().strip().lower()
        if option in ["y", "yes"]:
            # Create 1 subplot for each President.
            figure, (graph1, graph2) = plt.subplots(1, 2, figsize=(12, 6))

            # Get the years for the second President and filter available data.
            president1_years = range(president1.start_year, president1.end_year + 1)
            president1_years = [year for year in president1_years if minimum_year <= year <= maximum_year]

            # Filter the years to only include those for which data is available. 
            president1_inflation_data = [calculate_yoy_inflation(data, year) for year in president1_years if minimum_year <= year <= maximum_year]
            president1_unemployment_data = [calculate_unemployment_rate(data, year) for year in president1_years if minimum_year <= year <= maximum_year]

            # Plot the data for the first President. 
            graph1.set_title(f"{president1.name} ({president1.party})")
            graph1.plot(president1_years, president1_inflation_data, label=f"Inflation")
            graph1.plot(president1_years, president1_unemployment_data, label=f"Unemployment")
            graph1.set_xticks(president1_years)
            graph1.set_xlabel("Year")
            graph1.set_ylabel("Rate (%)")
            graph1.legend()

            # Get the years for the second President and filter available data.  
            president2_years = range(president2.start_year, president2.end_year + 1)
            president2_years = [year for year in president2_years if minimum_year <= year <= maximum_year]

            # Filter the years to only include those for which data is available.
            president2_inflation_data = [calculate_yoy_inflation(data, year) for year in president2_years if minimum_year <= year <= maximum_year]
            president2_unemployment_data = [calculate_unemployment_rate(data, year) for year in president2_years if minimum_year <= year <= maximum_year]

            # Plot the data for the second President.
            graph2.set_title(f"{president2.name} ({president2.party})")
            graph2.plot(president2_years, president2_inflation_data, label=f"Inflation")
            graph2.plot(president2_years, president2_unemployment_data, label=f"Unemployment")
            graph2.set_xticks(president2_years)
            graph2.set_xlabel("Year")
            graph2.set_ylabel("Rate (%)")
            graph2.legend()

            # Set the super title for the figure and show it. 
            figure.suptitle("Presidents Comparison")
            plt.show()

            # Prompt the user to save the visualization.
            save_visualization(f"./saved_graphs/{president1.name.lower().replace(' ', '_')}_{president2.name.lower().replace(' ', '_')}_comparison.png", figure)

        pause()
        break            

def compare_years_menu(data: tuple) -> None:
    """
    Opens the compare years menu.
    In this menu, the user can compare two years by inputting them.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        None
    """

    # Loop for persistent menu.
    while True:
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> COMPARISON MODE -> COMPARE YEARS\n")

        # Get the years from the user.
        year1 = ask_for_year(data)
        year2 = ask_for_year(data)

        # Check if the years are the same.
        if year1 == year2:
            fprint(Colors.RED + "You must compare two different years. Please try again.")
            pause()
            continue

        # Initialize the table with the row headers.
        table = [
            [f"{Colors.CYAN}Year"],
            [f"{Colors.CYAN}President in Office"],
            [f"{Colors.CYAN}Party in Office"],
            [f"{Colors.CYAN}Inflation Rate"],
            [f"{Colors.CYAN}Employment Rate"],
            [f"{Colors.CYAN}Unemployment Rate"]
        ]

        # Add data to the table.
        table[0].append(year1)
        table[0].append(year2)

        # Get political information for the given years.
        president1 = get_president(data, year1)
        president2 = get_president(data, year2)
        president1_color = get_party_color(president1.party)
        president2_color = get_party_color(president2.party)
        table[1].append(f"{president1_color}{president1.name}")
        table[1].append(f"{president2_color}{president2.name}")
        table[2].append(f"{president1_color}{president1.party}")
        table[2].append(f"{president2_color}{president2.party}")

        # Calculate the year-over-year inflation rate for each year.
        inflation1 = calculate_yoy_inflation(data, year1)
        inflation2 = calculate_yoy_inflation(data, year2)
        inflation_colors = get_comparison_colors(inflation1, inflation2)
        table[3].append(f"{inflation_colors[0]}{inflation1:.2f}%")
        table[3].append(f"{inflation_colors[1]}{inflation2:.2f}%")

        # Calculate the employment rate for each year.
        employment1 = calculate_employment_rate(data, year1)
        employment2 = calculate_employment_rate(data, year2)
        employment_colors = get_comparison_colors(employment1, employment2, inverted=True)
        table[4].append(f"{employment_colors[0]}{employment1:.2f}%")
        table[4].append(f"{employment_colors[1]}{employment2:.2f}%")

        # Calculate the unemployment rate for each year.
        unemployment1 = calculate_unemployment_rate(data, year1)
        unemployment2 = calculate_unemployment_rate(data, year2)
        unemployment_colors = get_comparison_colors(unemployment1, unemployment2)
        table[5].append(f"{unemployment_colors[0]}{unemployment1:.2f}%")
        table[5].append(f"{unemployment_colors[1]}{unemployment2:.2f}%")

        # Finally, print the table with string formatting.
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> COMPARISON MODE -> COMPARE YEARS\n")
        for row in table:
            fprint(f"{str(row[0]):<40} {str(row[1]):<30} {str(row[2]):<30}")

        # Ask the user if they would like to see a visualization of the data.
        fprint(f"\n{Colors.GREEN}Would you like to see a visualization of year comparison data? (y/n): {Colors.RESET}", end="")
        option = input().strip().lower()
        if option in ["y", "yes"]:
            # Constants for text sizes.
            TITLE_SIZE = 12
            LABEL_SIZE = 8
            SUPER_TITLE_SIZE = 14

            # Create a 2x2 grid of subplots for the data.
            figure, ((graph1, graph2), (graph3, graph4)) = plt.subplots(2, 2, figsize=(16, 9))

            # Create a line graph for monthly CPI data for the years.
            # Keep in mind that years with a large gap will have a large vertical gap in the graph.
            # This is due to the nature of the CPI metric and the economy.
            graph1.set_title("Monthly CPI Data", fontsize=TITLE_SIZE)
            # Plot the CPI data for each year per month.
            graph1.plot(range(1, 13), [get_cpi(data, year1, month) for month in range(1, 13)], label=str(year1))
            graph1.plot(range(1, 13), [get_cpi(data, year2, month) for month in range(1, 13)], label=str(year2))
            # Set the x-ticks to be the months.
            graph1.set_xticks(range(1, 13))
            graph1.set_xlabel("Month", fontsize=LABEL_SIZE)
            graph1.set_ylabel("CPI", fontsize=LABEL_SIZE)
            graph1.legend()

            # Create a bar graph for inflation rate data for the years.
            graph2.set_title("Inflation Rates", fontsize=TITLE_SIZE)
            # Plot the inflation rates for each year.
            # Year 1 is at x = 1, year 2 is at x = 2.
            graph2.bar([1, 2], [inflation1, inflation2])
            graph2.set_xlabel("Year", fontsize=LABEL_SIZE)
            graph2.set_ylabel("Rate (%)", fontsize=LABEL_SIZE)
            # Set the x-ticks to be the years.
            graph2.set_xticks([1, 2])
            graph2.set_xticklabels([str(year1), str(year2)])
            # Set the y-ticks to be in increments of 0.5.
            graph2.set_yticks(np.arange(np.max([inflation1, inflation2]) + 1, step=0.5))

            # Create a bar graph for employment rate data for the years.
            graph3.set_title("Employment Rates", fontsize=TITLE_SIZE)
            # Plot the employment rates for each year.
            # Year 1 is at x = 1, year 2 is at x = 2.
            graph3.bar([1, 2], [employment1, employment2])
            graph3.set_xlabel("Year", fontsize=LABEL_SIZE)
            graph3.set_ylabel("Rate (%)", fontsize=LABEL_SIZE)
            # Set the x-ticks to be the years.
            graph3.set_xticks([1, 2])
            graph3.set_xticklabels([str(year1), str(year2)])
            # Set the y-ticks to be in increments of 5.
            graph3.set_yticks(np.arange(np.max([employment1, employment2]) + 1, step=5))

            # Create a bar graph for unemployment rate data for the years.
            graph4.set_title("Unemployment Rates", fontsize=TITLE_SIZE)
            # Plot the unemployment rates for each year.
            # Year 1 is at x = 1, year 2 is at x = 2.
            graph4.bar([1, 2], [unemployment1, unemployment2])
            graph4.set_xlabel("Year", fontsize=LABEL_SIZE)
            graph4.set_ylabel("Rate (%)", fontsize=LABEL_SIZE)
            # Set the x-ticks to be the years.
            graph4.set_xticks([1, 2])
            graph4.set_xticklabels([str(year1), str(year2)])
            # Set the y-ticks to be in increments of 0.75.
            graph4.set_yticks(np.arange(np.max([unemployment1, unemployment2]) + 1, step=0.75))
            
            # Set the super title for the figure and show it.
            figure.suptitle("Year Comparison", fontsize=SUPER_TITLE_SIZE)
            plt.tight_layout()
            plt.show()

            # Prompt the user to save the visualization.
            save_visualization(f"./saved_graphs/{year1}_{year2}_comparison.png", figure)

        pause()
        break

def export_csv_menu(data: tuple) -> None:
    """
    Opens the export CSV menu.
    In this menu, the user is able to choose which data they would like to export to a CSV file.

    Parameters:
        data (tuple): A tuple containing all of the loaded data.

    Returns:
        None
    """

    # Loop for persistence.
    while True:
        # Print the title and section title, as well as the description.
        print_title()
        fprint(Colors.BOLD + "MAIN MENU -> EXPORT CSV")
        fprint("From this menu, you are able to export the calculated values from original datasets to your own CSV files.")
        fprint("This can be useful for further analysis or for sharing the data with others.")
        fprint("Please select the data you would like to export.\n")

        # Print menu.
        fprint("1. Export Inflation Data")
        fprint("2. Export Employment Data")
        fprint("0. Back to Main Menu")

        # Handle selection cases.
        option = input(Colors.GREEN + "\n> " + Colors.RESET).strip()
        # Match/case not used here as the options are a bit longer.
        # The first two options are partially the same, so they are handled together to reduce redundancy.
        if option == "1" or option == "2":
            # Get the year range compatible with all datasets.
            minimum_year, maximum_year = get_min_max_years(data)
            years = range(minimum_year, maximum_year + 1)

            # Initialize the data list with column headers.
            if option == "1":
                data_list = [
                    ["Year", "Inflation Rate (%)"]
                ]
            else:
                data_list = [
                    ["Year", "Employment Rate (%)", "Unemployment Rate (%)"]
                ]

            # Add data to the list.
            for year in years:
                if option == "1":
                    inflation = calculate_yoy_inflation(data, year)
                    data_list.append([year, inflation])
                else:
                    employment = calculate_employment_rate(data, year)
                    unemployment = calculate_unemployment_rate(data, year)
                    data_list.append([year, employment, unemployment])

            # Export the data to a CSV file.
            export_data(data_list)
        elif option == "0":
            main_menu(data)
            break
        else:
            fprint(Colors.RED + "Invalid option. Please try again.")
            pause()
                
def export_data(data: list) -> None:
    """
    Generic menu function to export data to a CSV file.
    This exists to reduce redundancy in the code.

    Parameters:
        data (list): A 2D list containing the data to export.
    
    Returns:
        None
    """

    # Get the file name from the user.
    fprint(f"\n{Colors.GREEN}Please enter the name of the file (without extension): {Colors.RESET}", end="")
    filename = input().strip()
    write_csv(filename + ".csv", data, True)
    pause()

def goodbye():
    """ 
    Prints a goodbye message.

    Parameters:
        None

    Returns:
        None
    """

    fprint(Colors.RED + "\nGoodbye!")


# MAIN FUNCTION

def main() -> None:
    data = load_data()
    main_menu(data)


# ENTRY POINT

if __name__ == "__main__":
    main()