import json

try:
    with open('geoworld.geojson', "r", encoding="utf") as data_file:
        data = json.load(data_file)

except Exception as e:
    print("Error: ", e, "\n")
    with open('geoworld.geojson', "r", encoding="utf-8-sig") as data_file:
        data = json.load(data_file)

print(data)