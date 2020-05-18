from recipe import Recipe
from book import Book
from time import sleep

if __name__ == '__main__':
    print("\nTest: allowed inputs for Recipe class.\n", "-" * 42)
    sandwich = Recipe("sandwich", 1, 10, ['ham', 'bread', 'cheese', 'tomatoes'], "lunch", "sandwich recipe.")
    print(str(sandwich))
    cake = Recipe("cake", 3, 60, ['flour', 'sugar', 'eggs'], "dessert", "cake recipe.")
    print(str(cake))
    salad = Recipe("salad", 2, 15, ['avocado', 'arugula', 'tomatoes', 'spinach'], "starter", "salad recipe.")
    print(str(salad))
    print("\nTest: allowed inputs for Book class.\n", "-" * 42)
    book = Book("My recipe book")
    print("Create Time: ", book.create_time)
    print("\nTest: Book class method.\n", "-" * 42)
    print("\nTest: add_recipe method")
    sleep(1)
    book.add_recipe(sandwich)
    print("Last Update Time: ", book.last_update)
    sleep(1)
    book.add_recipe(cake)
    print("Last Update Time: ", book.last_update)
    sleep(1)
    book.add_recipe(salad)
    print("Last Update Time: ", book.last_update)
    print("\nTest: get_recipes_by_type method.\n", "-" * 42)
    for recipe_type in ["starter", "dessert", "lunch"]:
        recipe_list = book.get_recipes_by_type(recipe_type)
        print("`{}` type recipe list is {}\n".format(recipe_type, recipe_list))
        for recipe_name in recipe_list:
            recipe = book.get_recipe_by_name(recipe_name)
    print("\nTest: invalid recipe_type for get_recipes_by_type\n", "-" * 42)
    book.get_recipes_by_type("42")
    print("\nTest: invalid recipe_name for get_recipes_by_name\n", "-" * 42)
    book.get_recipe_by_name("42")
    print("\nTest: invalid inputs for Recipe\n", "-" * 42)
    sleep(1)
    invalid = Recipe(1, "", "", "", 1, 1)


