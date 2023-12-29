# a possible alternative that is consistent with using with/as to load the json file from a local file path
import json
path = "cars.json"
with open(path, "r") as f:
    content = json.load(f)

for car in content["cars"]:
    for item in car.items():
        print(item[0], ':', item[1])
    print('\n')
