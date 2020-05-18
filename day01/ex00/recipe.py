class Recipe:
    name = ""
    cooking_lvl = 0
    cooking_time = 0
    ingredients = []
    recipe_type = ""
    description = ""

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        error_message = ""
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.recipe_type = recipe_type
        self.description = description

        if cooking_lvl not in range(1, 6):
            error_message += "`cooking_lvl` must be range 1 to 5. but it is \n"
        if not isinstance(cooking_time, int) or cooking_time < 0:
            error_message += "`cooking_time` must be positive numbers in minutes.\n"
        if not isinstance(ingredients, list):
            error_message += "`ingredients` must be list.\n"
        if recipe_type not in ["starter", "lunch", "dessert"]:
            error_message += "`recipe_type` must be \"starter\", \"lunch\" or \"dessert\".\n"

        if len(error_message) > 0:
            quit("InputError:\n"+error_message)

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "recipe name:\t{recipe.name}\n" \
              "description:\t{recipe.description}\n" \
              "cooking level:\t{recipe.cooking_lvl}\n"\
              "cooking time:\t{recipe.cooking_time}\n" \
              "ingredients:\t{recipe.ingredients}\n" \
              "recipe type:\t{recipe type}\n"
        return txt.format(recipe=self)
