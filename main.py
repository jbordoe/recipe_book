import json

global recipes


def main():
    recipes = load_recipes()
    print('WELCOME TO YOUR RECIPE BOOK!')

    while True:
        print(f'There Are Currently {len(recipes)} recipes')
        print("""
Please enter your desired option
0. Exit
1. Search for a Recipe
2. Add a New Recipe
    """)
        user_input = get_number_input(0, 2)
        if user_input == 0:
            print('Thanks for your time. Bye!')
            break
        elif user_input == 1:
            recipe_search()
        elif user_input == 2:
            new_recipe = create_recipe()
            recipes.append(new_recipe)
            save_recipes(recipes)


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


def recipe_search():
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
        name = ingredient['name']
        amount = ingredient['amount']
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
        ingredient_name = input('Please Enter Name of Ingredient, or "done" if you are finished: ')
        if ingredient_name == 'done':
            print(ingredients)
            break
        else:
            ingredient_amount = input(f'Please Enter Amount of {ingredient_name}')
            ingredient = {
                'name': ingredient_name,
                'amount': ingredient_amount
            }
            ingredients.append(ingredient)
            print(f'Added {ingredient_name}, {ingredient_amount}')
    recipe['ingredients'] = ingredients

    instructions = []
    while True:
        instruction = input(f'Please Enter Instruction {len(instructions) + 1}, or "done" if you are finished: ')
        if instruction == 'done':
            print(instructions)
            break
        else:
            instructions.append(instruction)
    recipe['instructions'] = instructions

    return recipe


main()