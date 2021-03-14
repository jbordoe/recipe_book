class Recipe:


    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def add_ingredient(self, name, amount):
        add_amt_ingredient = [name, amount]
        self.ingredients.append(add_amt_ingredient)

    def edit_ingredient(self, number, name=None, amount=None):
        if name:
            self.ingredients[number - 1][0] = name
        if amount:
            self.ingredients[number - 1][1] = amount


    def delete_ingredient(self, number):
        del self.ingredients[number - 1]

    def add_instruction(self, position, text):
        self.instructions.insert(position - 1, text)


    def move_instruction(self, old_position, new_position):
        if old_position < 1 or old_position > len(self.instructions):
            raise Exception('The number is too small or too large')
        if new_position < 1 or new_position > len(self.instructions):
            raise Exception('The number is too small or too large')
        self.instructions.insert(new_position - 1, self.instructions.pop(old_position - 1))

    def edit_instruction(self, position, text):
        del self.instructions[position - 1]
        self.instructions.insert(position - 1, text)

    def delete_instruction(self, position):
        del self.instructions[position - 1]
