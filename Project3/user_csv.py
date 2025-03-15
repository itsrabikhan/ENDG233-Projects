# user_csv.py
# ENDG 233 F24
# Rabi Khan, Daniel Yang
# GROUP 531
# A terminal-based data analysis and visualization program in Python.
# You must follow the specifications provided in the project description.
# Remember to include docstrings and comments throughout your code.

def read_csv(filename: str, include_headers: bool = True) -> list:
    """
    Read a CSV file and return the contents as a 2-dimensional list.
    This function assumes that the CSV file exists and is properly formatted.

    Parameters:
        filename (str): The name of file to read.
        include_headers (bool): Whether to include the first line as headers. Default to True

    Returns:
        list: 2 dimensional list containing the data from the CSV file.
    """
    
    result = []
    with open(filename, 'r') as file:
        # Read all lines from the CSV file and store them in a list.
        # If include_headers is False, exclude the first line.
        lines = file.readlines()
        lines = lines if include_headers else lines[1:]

        for line in lines:
            data = line.strip().split(',')

            for i in range(len(data)): 
                # Convert elements to a float if possible.
                try:
                    data[i] = float(data[i])
                except ValueError:
                    # If not possible, simply do nothing.
                    pass
            result.append(data)

    return result

def write_csv(filename: str, data, overwrite: bool) -> None:
    """
    Write data to a specified CSV file.

    Parameters:
        filenames (str): The name of the file to write to.
        data (list): The data to write to the file.
        overwrite (bool): Whether to overwrite the file if it already exists.

    Returns:
        None
    """

    # Open file with the selected mode.
    with open(filename, 'w' if overwrite else 'a') as file:
        # Write each row to file.
        for row in data:
            file.write(','.join([str(entry) for entry in row]) + '\n')