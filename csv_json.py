# Working with CSV files
from pathlib import Path
import json
import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "Count", "Price"])
    writer.writerow([1, 12, 5])
    writer.writerow([2, 15, 6])
    writer.writerow([1, 3, 9])

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Working with Json files
movies =[
    {"id":1, "Title":"myMovies1", "year":1990},
    {"id":2, "Title":"myMovies2", "year":1999},
    {"id":3, "Title":"myMovies3", "year":2999},
]

data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data)

data=Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0]["Title"])
print(movies[0]["year"])

