import csv
import random

def handle_cow_udder_count(udders):
    if udders == 4:
        if random.random() < 0.05:
            udders -= 1
    elif udders == 3:
        if random.random() < 0.20:
            udders = 4
    return udders

path = "Model/cows_and_goats.csv"

def update_cow_udder_count(animal_id, new_udders):
        rows = []
        updated = False

        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == animal_id:
                    row['Number of Udders'] = new_udders
                    updated = True
                rows.append(row)

        if updated:
            with open(path, mode='w', newline='') as file:
                fieldnames = ['ID', 'Age', 'Number of Udders']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)