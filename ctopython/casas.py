import csv

houses = {
    "Velasco": 0,
    "Goncalves": 0,
    "Azeredo": 0,
    "Rodrigues": 0
}
#= open casas.csv in read ("r") mode
with open("casas.csv", "r") as file:
    reader = csv.reader(file)
    next(reader) #to ignore the first line of the file
    for row in reader:
        house = row[1]
        houses[house] += 1 

for house in houses:
    count = houses[house]
    print(f"{house}: {count}")
