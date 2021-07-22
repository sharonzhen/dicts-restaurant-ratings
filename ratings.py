"""Restaurant rating lister.
    Reads the ratings in from the file
    Stores them in a dictionary
    And finally, spits out the ratings in alphabetical order by restaurant
"""

import random

def prints_ordered_dictionary(existing_dictionary):
    for key, value in sorted(existing_dictionary.items()):
        print(f"{key} is rated at {value}.")


def add_new_rating(existing_dictionary, key = None):
    """
    Prompt the user for a restaurant name
    Prompt the user for a restaurant score
    Store the new restaurant/rating in the dictionary
    Print all of the ratings in alphabetical order (including the new one, of course)
    """
    if key:
        print(f'Please assign a rating for {key}!')
        res_name = key
    else: 
        print('Please assign a rating for your restaurant!')
        res_name = input('Restaurant name: ')

    rating = int(input('Rating: '))
    if rating in range(6):
        existing_dictionary[res_name] = rating
    else:
        print("Please return a valid rating from 1-5")
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
    
    
def get_random_key(existing_dictionary):
    random_key = random.choice(list(existing_dictionary.keys()))
    return random_key

def choose_a_restaurant(existing_dictionary):
    print("Here's a list of existing restaurants: ")
    prints_ordered_dictionary(existing_dictionary)
    res_name = input('What restaurants would you like to update the rating? ')
    # check if restaurant_name in existing_dictionary using .get()
    if existing_dictionary.get(res_name, 0):
        add_new_rating(existing_dictionary, res_name)
    else: 
        ans = input('Your input is not listed. Would you like to add anyway? (y/n) ').lower()
        if ans == 'y':
            add_new_rating(existing_dictionary, res_name)

    return existing_dictionary

def main():
    restaurant_dict = {}
    restaurant_dict = convert_file_to_dictionary("scores.txt", restaurant_dict)
    while True:
        user_prompt = input("Would you like to \n\
                                (a) rate a restaurant\n\
                                (b) see ratings\n\
                                (c) quit \n\
                                (d) update a random restaurant rating\n\
                                (e) choose a restaurant to rate\n").lower()
        if user_prompt == 'a':
            restaurant_dict = add_new_rating(restaurant_dict)
        elif user_prompt == 'b':
            prints_ordered_dictionary(restaurant_dict)
        elif user_prompt == 'c':
            break
        elif user_prompt == 'd':
            rand_key = get_random_key(restaurant_dict)
            restaurant_dict = add_new_rating(restaurant_dict, rand_key)
        elif user_prompt == 'e':
            restaurant_dict = choose_a_restaurant(restaurant_dict)
        else: 
            print("Please enter a valid choice (a)-(e)")
    prints_ordered_dictionary(restaurant_dict)

def display_currdir():
    """ display list of text files in current directory
    """
def file_to_upload():
    """ lets user choose file to upload, uploads file
    """

if __name__ == "__main__":
    """
    Modify your script so that it displays a list of text files in 
    current directory and allows the users to upload other files. 
    Now we can keep the ratings for different types of restaurants. 
    Allow the user to leave one list and open another.
    """
    
