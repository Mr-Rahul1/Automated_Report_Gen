import csv

data = [
    ['Name', 'Sales', 'Region'],
    ['Alice', 1200, 'North'],
    ['Bob', 1500, 'South'],
    ['Charlie', 700, 'East'],
    ['Diana', 1300, 'West'],
    ['Eve', 1600, 'North']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created as data.csv")
