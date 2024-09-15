from Model.check_id import check_animal_data
from Model.update_udders import update_cow_udder_count, handle_cow_udder_count

def cal_milk(animal_id, udders, age):
    if udders == 4:
        milk_production = calculate_milk_production(age)
    else:
        milk_production = 0
    updated_udders = handle_cow_udder_count(udders)
    update_cow_udder_count(animal_id, updated_udders)
    return milk_production


def calculate_milk_production(age):
    try:
        # Split the age into years and months
        age_parts = age.split(' years, ')
        years = int(age_parts[0]) if age_parts[0] else 0
        # Extract months
        months = age_parts[1].split(' months')[0]
        months = int(months) if months else 0
    except (IndexError, ValueError):
        # Handle the case where the input format is incorrect
        years = 0
        months = 0

    return years + months
