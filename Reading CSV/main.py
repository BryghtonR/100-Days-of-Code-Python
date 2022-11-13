import pandas

#data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print(int(monday.temp) * 1.8 + 32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirels_count)
print(cinnamon_squirels_count)
print(black_squirels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirels_count, cinnamon_squirels_count, black_squirels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squire_count.csv")