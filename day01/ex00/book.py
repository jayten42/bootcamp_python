from datetime import datetime
from recipe import Recipe


class Book:
    name = ""
    create_time = datetime.now()
    last_update = create_time
    recipes_list = {
        'starter': [],
        'lunch': [],
        'dessert': [],
    }

    def __init__(self, name):
        self.name = name
        self.create_time = datetime.now()
        self.last_update = self.create_time

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        all_recipes = sum(self.recipes_list.values(), [])
        for recipe in all_recipes:
            if recipe.name == name:
                print(recipe)
                return recipe
        print("{} is not in this book.".format(name))
        return None

    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if recipe_type not in self.recipes_list:
            print("{} is invalid recipe type.".format(recipe_type))
            return
        recipe_names = [recipe.name for recipe in self.recipes_list[recipe_type]]
        return recipe_names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("recipe is not instance of Recipe")
            return
        recipe_type = recipe.recipe_type
        self.recipes_list[recipe_type].append(recipe)
        self.last_update = datetime.now()

