import csv

file_route = "area_protegida.csv"

def print_report(title, *args):
    print(f"{title.capitalize():-^40}")
    for elem in args:
        print(f"{elem[0]}: {elem[1]}")


with open(file_route, "r", encoding="utf-8") as data_set:
    reader = csv.reader(data_set)
    header, data = next(reader), list(reader)

my_data = {}

for row in data:
    if row[6] in my_data:
        my_data[row[6]] += 1
    else:
        my_data[row[6]] = 1

top_rating = sorted(my_data.items(), key=lambda x: x[1], reverse=True)[:5]
print_report("Super listado", top_rating[0], top_rating[1], top_rating[2])