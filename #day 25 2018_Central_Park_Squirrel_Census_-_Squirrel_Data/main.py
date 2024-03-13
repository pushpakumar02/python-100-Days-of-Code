import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240309.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "squirrels": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
dt = pandas.DataFrame(data_dict)
dt.to_csv("squirrel_count.csv")




# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)



# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# average_temp = data["temp"].max()
# print("max_temperature: ",average_temp)
# print(data[data["day"] == "Monday"])
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# get data from rows
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)
# create a dataframe from scratch

#
# data_dict = {
#     "students": ["pushpa", "kumar", "dinesh"],
#     "score": [35, 45, 55]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data_csv")



