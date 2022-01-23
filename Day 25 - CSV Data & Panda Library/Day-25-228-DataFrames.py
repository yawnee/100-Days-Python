# Comments
# A Series = list (single column)
# Ref: https://pandas.pydata.org/docs/
# Ref: https://pandas.pydata.org/docs/reference/index.html


import pandas

# Panda Example:
data = pandas.read_csv("weather_data.csv")

# Prints the csv into a nicely presented table
print(data)
print("")

# Prints the csv into a nicely presented table
print(type(data))
# Prints only the temperature
print(data["temp"])
print("")

#  Converting to dictionary
data_dict = data.to_dict()
print(data_dict)
print("")

# Calculating average with out pandas
temp_list = data["temp"].to_list()
print(temp_list)
average = sum(temp_list) / len(temp_list)
print(average)
print("")

# Math operation
print(data["temp"].mean())  # average value simplified
print(data["temp"].max())  # max value
print("")

# Get Data in Columns
print(data["condition"])
print(data.condition)
print("")

# Get Data in a Row
print(data[data.day == "Monday"])
print("")

# Get the max temperature row
print(data[data.temp == data.temp.max()])
print("")

# Finding the temperature of a specific day and then converting to F
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 /5 + 32
print(monday_temp_F)
print("")

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")




