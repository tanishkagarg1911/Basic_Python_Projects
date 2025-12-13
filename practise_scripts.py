import csv
import pandas as pd

data = [
    ["name", "age", "city"],
    ["John", 19, "Ghaziabad"],
    ["Aisha", 20, "Delhi"],
    ["Rahul", 21, "Noida"],
    ["Sneha", 18, "Meerut"],
    ["Arjun", 22, "Gurgaon"],
    ["Priya", 20, "Faridabad"],
    ["Karan", 23, "Delhi"],
    ["Neha", 19, "Ghaziabad"],
    ["Rohit", 21, "Noida"],
    ["Ananya", 22, "Delhi"]
]
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

df=pd.read_csv('data.csv')
print("rows: ", len(df))
