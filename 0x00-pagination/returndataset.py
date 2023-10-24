import csv
DATA_FILE = "Popular_Baby_Names.csv"
with open(DATA_FILE) as f:
        reader = csv.reader(f)
        dataset = [row for row in reader]

print(dataset)