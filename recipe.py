class Recipe:


    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def add_ingredient(self, name, amount):
        add_amt_ingredient = [name, amount]
        self.ingredients.append(add_amt_ingredient)

    def edit_ingredient(self, number, name, amount):
        add_amt_ingredient = [name, amount]
        del self.ingredients[number - 1]
        self.ingredients.append(add_amt_ingredient)
#TODO: create a test of edit ingredient (if you don edit name it keeps the name, just like the amount)