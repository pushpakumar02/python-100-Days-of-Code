import requests
from datetime import datetime

USERNAME = "pushpakumar"
TOKEN = "..."
GRAPH_ID = "graph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

new_unit = "hours"
graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": new_unit,
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many Hours did you code today? "),
}

response = requests.post(pixel_creation_endpoint,json=pixel_data, headers=headers)
print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
#
#
# new_pixel_data = {
#     "quantity": "4.00"
# }
#
# # response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# # print(response.text)
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"
#
# # response = requests.delete(url=delete_endpoint, headers=headers)
# # print(response.text)
# https://pixe.la/v1/users/pushpakumar/graphs/graph.html
