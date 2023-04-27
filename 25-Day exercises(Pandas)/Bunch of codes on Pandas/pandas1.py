import pandas

data = pandas.read_csv('weather_data.csv')
data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(temp_list)

# 1 way of finding an average of a temperatures
average = sum(temp_list) / len(temp_list)
print(average)

# 2 way of finding an average of a temperatures
# Get data in columns
print(data['temp'].mean())
print(data['temp'].max())

# Get data in a row
print(data[data.day == "Monday"])

# Get the data with the highest temperature row
print(data[data.temp == data.temp.max()])

# Convert Mondays temperature to Fahrenheit
monday = data[data.day == "Monday"]
print(monday)
monday_temp = int(monday.temp)
print(int(monday.temp[0]))
print(monday_temp)
fahrenheit = monday.temp * 1.8 + 32
print(fahrenheit)

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)