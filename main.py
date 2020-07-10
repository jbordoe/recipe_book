import json

global recipes
global selected_recipe

def main():
    global recipes
    recipes = load_recipes()
    print('WELCOME TO YOUR RECIPE BOOK!')

    while True:
        print(f'There Are Currently {len(recipes)} recipes')
        print("""
Please enter your desired option
0. Exit
1. Search for a Recipe
2. Add a New Recipe
3. Make changes to existing Recipe (Update)
4. Delete Recipe
    """)
        user_input = get_number_input(0, 4)
        if user_input == 0:
            print('Thanks for your time. Bye!')
            break
        elif user_input == 1:
            recipe_search()
        elif user_input == 2:
            new_recipe = create_recipe()
            recipes.append(new_recipe)
            save_recipes(recipes)
        elif user_input == 3:
            update_recipe()
        elif user_input == 4:
            delete_recipe()
# convert python data structure into JSON string

def save_recipes(recipes):
    json_string = json.dumps(recipes)
    f = open('recipes.json', 'w')
    f.write(json_string)
    f.close()


def load_recipes():
    f = open('recipes.json', 'r')
    recipes_string = f.read()
    f.close()
    return json.loads(recipes_string)


def get_number_input(min, max):
    while True:
        user_input = input()
        try:
            user_int = int(user_input)
            if user_int < min or user_int > max:
                print(f'Please enter a number between {min} and {max}')
                continue
            return user_int
        except ValueError:
            print('You did not enter a number.')

def yes_no(text):
    name_answer = input(text).lower()
    yes_or_no = ['y', 'yes', 'no', 'n']
    while name_answer not in yes_or_no:
        print('Please input yes(y) or no(n)')
        name_answer = input('y/n: ').lower()
        print(name_answer)
    if name_answer == 'no' or name_answer == 'n':
        return False
    elif name_answer == 'yes' or name_answer == 'y':
        return True

def find_recipe():
    global selected_recipe
    global recipes
    while True:
        query = input('Enter your search term: ')

        matches = list(filter(lambda x: query.lower() in x['name'].lower(), recipes))

        print(f'Found {len(matches)} match(es)!')

        if len(matches) == 0:
            if yes_no('Do you want to try a new search? '):
                continue
            else:
                return False


        names = list(map(lambda x: x['name'], matches))

        print('0. Return to Main Menu')
        for i, name in enumerate(names):
            print(f'{i + 1}. {name}\n')

        print('Enter a number related to the food (match) you are interested: ')
        num_input = get_number_input(0, len(matches))
        if num_input == 0:
            'Returning to main menu'
            return False
        else:
            selected_recipe = matches[num_input - 1]

            print(f'These are the details of your choice:')
            display_recipe(selected_recipe)
            return True

def recipe_search():
    global recipes
    while True:
        query = input('Enter your search term: ')

        matches = list(filter(lambda x: query.lower() in x['name'].lower(), recipes))

        print(f'Found {len(matches)} match(es)!')

        names = list(map(lambda x: x['name'], matches))

        print('0. Return to Main Menu')
        for i in range(0, len(names)):
            print(f'{i + 1}. {names[i]}\n')

        print('Enter a number related to the food (match) you are interested: ')
        num_input = get_number_input(0, len(matches))
        if num_input == 0:
            'Returning to main menu'
            break
        else:
            selected_recipe = matches[num_input - 1]

            print(f'These are the details of your choice:')
            display_recipe(selected_recipe)


def display_recipe(recipe):
    recipe_name = recipe['name'].upper()
    print(f'How to cook {recipe_name}')
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        name = ingredient[0]
        amount = ingredient[1]
        print(f'  {name}, {amount}')
    print('Instructions:')
    step_n = 1
    for step in recipe['instructions']:
        print(f'  {step_n}: {step}')
        step_n += 1


def create_recipe():
    recipe = {}
    name_food = input('What food do you want to add to the recipe book?'.capitalize())
    recipe['name'] = name_food

    ingredients = []
    while True:
        ingredient_name = input('Please Enter Name of Ingredient, or "done" if you are finished:\n')
        if ingredient_name == 'done':
            print(ingredients)
            break
        else:
            ingredient_amount = input(f'Please Enter Amount of {ingredient_name}:\n')
            ingredient = {
                'name': ingredient_name,
                'amount': ingredient_amount
            }
            ingredients.append(ingredient)
            print(f'Added {ingredient_name}, {ingredient_amount}')
    recipe['ingredients'] = ingredients

    instructions = []
    while True:
        instruction = input(f'Please Enter Instruction {len(instructions) + 1}, or "done" if you are finished:\n')
        if instruction == 'done':
            print(instructions)
            break
        else:
            instructions.append(instruction)
    recipe['instructions'] = instructions

    return recipe

def update_recipe_instructions():
    global selected_recipe
    while True:
        print("""
    Please enter your desired option
    0. Done
    1. Add to existing instructions
    2. Update
    3. Delete
        """)
        user_input = get_number_input(0, 3)
        instructions = selected_recipe['instructions']
        if user_input == 0:
            break
        elif user_input == 1:
            add_instruction = input('Enter the instruction and the preferred position of this instruction below:\n')
            position_instruction = int(input('Enter the number related to the instruction:\n'))
            instructions.insert(position_instruction - 1, add_instruction)
            break
        elif user_input == 2:
            print('Enter the number of the instruction you want to edit:\n')
            edit_instruction_num = get_number_input(1, len(instructions))
            edit_instruction = input('Re-enter the instruction here to edit:\n')
            del instructions[edit_instruction_num - 1]
            instructions.insert(edit_instruction_num - 1, edit_instruction)
            break
        elif user_input == 3:
            print('Enter the number of the instruction you want to delete:\n')
            delete_num = get_number_input(1, len(instructions))
            del instructions[delete_num - 1]
            print('Instruction Deleted!')
            #TODO Handle the case when the instruction is empty

def update_recipe_ingredients():
    global selected_recipe

    while True:
        print("""
    Please enter your desired option
    0. Done
    1. Add to existing ingredients
    2. Update
    3. Delete
        """)
        user_input = get_number_input(0, 3)
        ingredient = selected_recipe['ingredients']
        if user_input == 0:
            break
        elif user_input == 1:
            add_ingredients = input('Enter the name of the ingredients:\n')
            amount_ingredients = input('Enter the amount of ingredient:\n')
            add_amt_ingredient = add_ingredients, amount_ingredients
            ingredient.append(add_amt_ingredient)
            break
        elif user_input == 2:
            print('Enter the number of the ingredient you want to edit:\n')
            edit_ingredients_num = get_number_input(1, len(ingredient))
            add_ingredients = input('Enter the name of the ingredients:\n')
            amount_ingredients = input('Enter the amount of ingredient:\n')
            add_amt_ingredient = add_ingredients, amount_ingredients
            del ingredient[edit_ingredients_num - 1]
            ingredient.append(add_amt_ingredient)
            break
        elif user_input == 3:
            print('Enter the number of the ingredient you want to delete:\n')
            del_num = get_number_input(1, len(ingredient))
            del ingredient[del_num - 1]
            print('ingredients Deleted!')


def update_recipe():
    global selected_recipe
    global recipes
    result = find_recipe()
    if result:
        name_answer = yes_no("""Do you want to make changes to the name of the food you selected?
        \nPlease input Yes(y) or No(n): """)
        if not name_answer:
            print(f"Great the food name: {selected_recipe['name']} is maintained!")
        else:
            update_name = input('Enter a new name for the food you are updating:\n')
            selected_recipe['name'] = update_name

        instruction_answer = yes_no("""Do you want to make changes to the instructions of the food you selected?
        \nPlease input Yes(y) or No(n): """)
        if not instruction_answer:
            print(f"Great! The instruction are  maintained!")
        else:
            update_recipe_instructions()
        save_recipes(recipes)
        ingredient_answer = yes_no("""Do you want to make changes to the ingredients of the food you selected?
                \nPlease input Yes(y) or No(n): """)
        if not ingredient_answer:
            print(f"Great! The ingredients are  maintained!")
        else:
            update_recipe_ingredients()
        save_recipes(recipes)
    #TODO Show the updated recipe (selected_recipe)
    else:
        print('Returning to Main Menu')


def delete_recipe():
    global selected_recipe
    global recipes
    result = find_recipe()
    delete_answer = yes_no("""Are you sure you want to DELETE this recipe?
    \nPlease input Yes(y) or No(n): """)
    if not delete_answer:
        print(f"Great! The recipe for: {selected_recipe['name']} is maintained!")
    else:
        del selected_recipe
    save_recipes(recipes)
    print('Recipe Deleted!')



main()

# TODO: Add Update functionality
# 1. Add update option to main menu
# 2. IF user decides to update, they can search for a recipe
# 3. Upon selecting a recipe the recipe is displayed to them
# 4. User decides if they want to add, or update something in the recipe
# 5. We add or update based on the user input

# TODO
# 1. Add an instruction(user should be able to type an instruction and update on their preferred position in the instruction list)
# 2. Edit an instruction(same number of instruction but individual instructions can be edited)
# 3. Do 1, 2, and delete to ingredients
# 4. Deleting Recipes

#Done with
