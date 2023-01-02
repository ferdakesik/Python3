
import csv

# with open("ferda.csv") as file:
#     print(file.read())


with open("ferda.csv") as file:
    csv_reader=csv.reader(file)
    for f in csv_reader:
        print(f)


