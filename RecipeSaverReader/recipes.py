'''
Yiming Ge
CS 5001, Fall 2021
HW06 -- Problem 2

This is a a program that will enable users to save and read recipes.
'''


def menu_validation(choice):
    '''
        Function -- menu_validation
            check whether the given choice is valid
        Parameter:
            choice -- given choice (can not be an integer)
        Returns:
            Return True if choice is either 1, 2 or 3.
            Otherwise False
    '''
    try:
        choice = int(choice)
        if choice == 1 or choice == 2 or choice == 3:
            return True
        return False
    except ValueError:
        return False


def final_validation(input_string, invalid_string, validation_function,
                     trans_function=None):
    '''
        Function -- finl_validation
            If user's input is invalid, print invalid string
            then repeat the prompt until he gets it right.
        Parameter:
            input_string -- the string prompt to user
            invalid_string -- if user's input is invalid, print invalid string
            validation_function -- function to do validation of the input
            trans_function -- the function to transform the user input
        Returns:
            Return a valid user input
    '''
    user_input = input(input_string)
    if trans_function:
        user_input = trans_function(user_input)
    while validation_function(user_input) is False:
        print(invalid_string)
        user_input = input(input_string)
        if trans_function:
            user_input = trans_function(user_input)
    return user_input


def trans_to_ingredients_list(ingredients):
    '''
        Function -- trans_to_ingredients_list
            Split the input string into a list at the commas and remove any
            leading or trailing whitespace from each item.
        Parameter:
            ingredients -- ingredients string
        Returns:
            Return a clean ingredient list
    '''
    clean_ingredients_list = []
    ingredients_list = ingredients.split(',')
    for ingredient in ingredients_list:
        clean_ingredients_list.append(ingredient.strip())
    return clean_ingredients_list


def ingredients_validation(ingredients):
    '''
        Function -- ingredients_validation
            check whether the given ingreients are valid.
        Parameter:
            ingredients -- a list of ingredients including empty list
        Returns:
            Return True if the ingredient list contain at least one non-empty
            string. Otherwise return False
    '''
    if len(ingredients) >= 1 and ingredients.count("") <= len(ingredients) - 1:
        return True
    return False


def time_validation(time):
    '''
        Function -- time_validation
            check whether the given time is valid.
        Parameter:
            time -- given time (can not be an integer)
        Returns:
            Return True if time is an integer greater than or equal to 0.
            Otherwise return False.
    '''
    try:
        time = int(time)
        if time < 0:
            return False
        return True
    except ValueError:
        return False


def convert_recipe_name(name):
    '''
        Function -- convert_recipe_name
            convert the recipe name to lowercase, remove any leading or
            trailing whitespace, convert any other white space to underscores,
            then remove any remaining non-alphanumeric characters
            and add “.txt” to the end.
        Parameter:
            name -- given recipe name
        Returns:
            Return the name after conversion
    '''
    name = name.lower()
    name = name.strip()
    name = name.replace(" ", "_")
    name = ''.join([string for string in name if string.isalnum() or
                    string == "_"])
    return name + ".txt"


def contents(name, ingredients, directions, time):
    '''
        Function -- contents
            combine the given information in required format
        Parameter:
            name -- given recipe name by user
            ingredients -- valid given ingredients list
            directions -- directions given by user
            time -- valid time given by user
        Returns:
            Return the contents -- the combination of given info
    '''
    name_content = name
    ingredients_content = "Ingredients:\n" + '\n'.join(ingredients)
    time_content = "Time: {} minutes".format(time)
    directions_content = "Directions:\n" + directions
    contents = name_content + 2 * '\n' \
                            + ingredients_content + 2 * '\n'\
                            + time_content + 2 * '\n' \
                            + directions_content
    return contents


def save_recipe(recipe_name, contents):
    '''
        Function -- save_recipe
            Writes contents to a file.
        Parameter:
            recipe_name -- save the file using this name
            contents -- contents written into the file
        Returns:
            Nothing.
    '''
    file = open(recipe_name, "w")
    file.write(contents)
    file.close()


def read_recipe(recipe_name):
    '''
        Function -- read_recipe
            Reads an entire recipe
        Parameter:
            recipe_name -- the file name
        Returns:
            The contents of the recipe (a string)
    '''
    file = open(recipe_name, "r")
    recipe_contents = file.read()
    file.close()
    return recipe_contents


def main():
    SAVE = "1"
    READ = "2"
    QUIT = "3"
    CHOICE_STRING = "MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit "
    INVALID_CHOICE = 'Invalid choice'
    INGREDIENTS_STRING = "Enter the ingredients on one line. " + \
                         "Separate each ingredient with a comma. "
    INVALID_INGREDIENTS = "Recipe must have at least one ingredient."
    TIME_STRING = "Enter the time needed in minutes: "
    INVALID_TIME = "Invalid time. Must be an integer " + \
                   "greater than or equal to 0."
    # prompt the user to choose what they would like to do from this menu
    choice = final_validation(CHOICE_STRING, INVALID_CHOICE, menu_validation)
    while choice != QUIT:
        if choice == SAVE:
            # prompt the user to enter ingredients
            ingredients = final_validation(INGREDIENTS_STRING,
                                           INVALID_INGREDIENTS,
                                           ingredients_validation,
                                           trans_to_ingredients_list)
            # prompt the user to enter directions
            directions = input("Enter the directions (1 paragraph only): ")
            # prompt the user to enter time
            time = final_validation(TIME_STRING, INVALID_TIME, time_validation)
            # prompt the user to enter recipe name
            name = input("Enter the name of the recipe: ")
            recipe_name = convert_recipe_name(name)
            while recipe_name == ".txt":
                print("Unable to create the filename.")
                name = input("Enter a string containing only letters, "
                             "numbers, and spaces ")
                recipe_name = convert_recipe_name(name)
            # combine all the given info with given format
            saving_contents = contents(name, ingredients, directions, time)
            # save the recipe
            save_recipe(recipe_name, saving_contents)
            print("{} recipe saved to {}".format(name, recipe_name))
        if choice == READ:
            # prompt the user to enter the name of recipe
            name = input("Enter the name of the recipe: ")
            recipe_name = convert_recipe_name(name)
            try:
                print(read_recipe(recipe_name))
            except FileNotFoundError:
                print("Unable to print {}".format(recipe_name))
        # prompt the user to select choice from menue again
        choice = final_validation(CHOICE_STRING, INVALID_CHOICE,
                                  menu_validation)


if __name__ == "__main__":
    main()
