from Model.check_id import check_animal_data

def validate_input(animal_id):
    # check the data entered a number and check data have 8 length and check first animal_id number is not 0
    if not animal_id.isdigit() or len(animal_id) != 8 or animal_id[0] == '0':
        return None, 0, None
    else:
        return check_animal_data(animal_id)
    
