def print_recipe(name):
    recipe = cookbook[name]
    fmt = "Recipe for {}:\n" \
          "Ingredients list: {}\n" \
          "To be eaten for {}\n" \
          "Takes {} minutes of cooking."
    print(fmt.format(name, recipe['ingredients'], recipe['meal'], recipe['prep_time']))


def delete_recipe(name):
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }


def print_all_recipe():
    print('Cookbook')
    print('-' * 42)
    for name in cookbook.keys():
        print_recipe(name)
        print('-'*42)


if __name__ == '__main__':
    cookbook = {
        'sandwich': {
            'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
            'meal': 'lunch',
            'prep_time': 10
        },
        'cake': {
            'ingredients': ['flour', 'sugar', 'eggs'],
            'meal': 'dessert',
            'prep_time': 60
        },
        'salad': {
            'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
            'meal': 'lunch',
            'prep_time': 15
        },
    }
    while True:
        print("Please select an option by typing the corresponding number:\n"
              "1: Add a recipe\n"
              "2: Delete a recipe\n"
              "3: Print a recipe\n"
              "4: Print the cookbook\n"
              "5: Quit")
        try:
            option = int(input(">> "))
            if option < 1 or option > 5:
                raise ValueError
        except ValueError:
            while True:
                try:
                    option = int(input("This option does not exist, please type the corresponding number.\n"
                                       "To exit, enter 5.\n"
                                       ">> "))
                    if option < 1 or option > 5:
                        raise ValueError
                    break
                except ValueError:
                    pass

        if option == 1:
            name = input("Please enter the New recipe's name to add.\n"
                         ">> ")
            ingredients = input("Please enter the Ingredients separated by ','\n"
                                ">> ").split(',')
            meal = input("Please enter the type of meal.\n"
                         ">> ")
            try:
                prep_time = int(input("Please enter the preparation time in minutes.\n"
                                      ">> "))
            except ValueError:
                while True:
                    try:
                        prep_time = int(input("preparation time is must number\n"
                                              ">> "))
                        break
                    except ValueError:
                        pass
            add_recipe(name, ingredients, meal, prep_time)
            print("Successfully add {}'s recipe.".format(name))
        elif option == 2:
            name = input("Please enter the recipe's name to delete.\n"
                         ">> ")
            delete_recipe(name)
            print("Successfully Delete {}'s recipe.".format(name))
        elif option == 3:
            name = input("Please enter the recipe's name to get its details.\n"
                         ">> ")
            print_recipe(name)
        elif option == 4:
            print_all_recipe()
        else:
            quit("Cookbook closed.")
