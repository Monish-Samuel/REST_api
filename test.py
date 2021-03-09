import requests

Base = "http://127.0.0.1:5000/"

data = [{'likes': 10, 'name': 'Hello world', 'views': 1100},
        {'likes': 12, 'name': 'Bimbo', 'views': 11851},
        {'likes': 125, 'name': 'Food', 'views': 158520},
        {'likes': 12547, 'name': 'Tourist', 'views': 100},
        {'likes': 178, 'name': 'Travel', 'views': 18500},
        {'likes': 1781, 'name': 'Pets', 'views': 18760}]

for i in range(len(data)):
    response = requests.put(Base + "channel/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(Base + "channel/2")
print(response.json())

