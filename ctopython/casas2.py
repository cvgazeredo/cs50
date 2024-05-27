import csv

houses = {
    "Velasco": 0,
    "Goncalves": 0,
    "Azeredo": 0,
    "Rodrigues": 0
}

with open("casas.csv", "r") as file:
    reader = csv.DictReader(file)
    next(reader)
    for row in reader:
        house = row["Casas"]
        houses[house] += 1

for house in houses:
    count = houses[house]
    print(f"{house}: {count}")
