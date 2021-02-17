import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 55, "name":"jaler", "views": 500},
#         {"likes": 10, "name":"sekar", "views": 2323},
#         {"likes": 500, "name":"maji mantab", "views": 19000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())


# input()
response = requests.patch(BASE + "video/2", {"likes": 101,"views":99})
print(response.json())
