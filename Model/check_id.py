import csv

path = "Model/cows_and_goats.csv"

def check_animal_data(animal_id):
    with open(path, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row['ID'] == animal_id:
                udders = row.get('Number of Udders', '')
                age = row.get('Age', '')

                if age == '' and udders == '':
                    return "goat", 0, None
                
                if udders:
                    udders = int(udders)
                    return "cow", udders, age
        return "unknown", 0, None
