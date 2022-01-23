# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv  # Used for manging csv files
import pandas  # Used for managing csv files more efficiently

# Reading data for a specific column, in this case, column 2 (temperature)
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

print("")

# Panda Example:
# Prints the csv into a nicely presented table
data = pandas.read_csv("weather_data.csv")
print(data)
# Prints only the temperature
print(data["temp"])
