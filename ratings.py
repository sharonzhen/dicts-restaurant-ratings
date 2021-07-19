"""Restaurant rating lister.
    Reads the ratings in from the file
    Stores them in a dictionary
    And finally, spits out the ratings in alphabetical order by restaurant

"""

def prints_dictionary(existing_dictionary):
    for key, value in existing_dictionary.items():
        print(f"{key} is rated at {value}.")


def add_new_rating(existing_dictionary):
    """
    Prompt the user for a restaurant name
    Prompt the user for a restaurant score
    Store the new restaurant/rating in the dictionary
    Print all of the ratings in alphabetical order (including the new one, of course)
    """
    print('Please assign a rating for your restaurant!')
    res_name = input('Restaurant name: ')
    rating = int(input('Rating: '))

    existing_dictionary[res_name] = rating
    return existing_dictionary

    

def convert_file_to_dictionary(textfile, existing_dictionary):
    the_file = open(textfile)
    for line in the_file:
        line = line.rstrip().split(':')
        name = line[0]
        score = line[1]
        existing_dictionary[name] = score
    
    the_file.close()
    return existing_dictionary


if __name__ == "__main__":
    restaurant_dict = {}
    restaurant_dict = convert_file_to_dictionary("scores.txt", restaurant_dict)
    while True:
        user_prompt = input("Would you like to rate a restaurant? (y/n) ").lower()
        if user_prompt == 'y':
            restaurant_dict = add_new_rating(restaurant_dict)
        else: 
            break
    prints_dictionary(restaurant_dict)
