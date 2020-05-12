class Recipe:
    name = ""
    cooking_lvl = 0
    cooking_time = 0
    ingredients = []
    recipe_type = ""
    description = ""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "recipe name:\t{recipe.name}\n" \
              "description:\t{recipe.description}\n" \
              "cooking level:\t{recipe.cooking_lvl}\n"\
              "cooking time:\t{recipe.cooking_time}\n" \
              "ingredients:\t{recipe.ingredients}\n" \
              "recipe type:\t{recipe type}\n"
        return txt.format(recipe=self)
