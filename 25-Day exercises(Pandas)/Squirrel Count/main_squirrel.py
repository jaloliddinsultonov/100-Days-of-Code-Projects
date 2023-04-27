import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = 0
cinnamon = 0
black = 0

for squirrel in data['Primary Fur Color']:
    if squirrel == "Gray":
        gray += 1
    elif squirrel == "Cinnamon":
        cinnamon += 1
    elif squirrel == 'Black':
        black += 1

data_dict = {
    'Fur Color': ["Gray", "Cinnamon", "Black"],
    'Count': [gray, cinnamon, black]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_data.csv")
print(data)


# 2nd way

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrel_count = len(data[data['Primary Fur Color'] == "Black"])

data_dict = {
    'Fur Color': ["Gray", "Cinnamon", "Black"],
    'Count': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data.csv")



