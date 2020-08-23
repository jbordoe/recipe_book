import json
import getpass
from passlib.context import CryptContext
from input_handler import get_string, get_number_input, yes_no
from instructions_handler import add_instructions, move_instruction
from ingredients_handler import add_ingredients, edit_ingredients
from search_handler import recipe_search, recipe_search_ingredients



def main():
    global recipes
    global selected_recipe
    recipes = load_recipes()
    print('WELCOME TO YOUR RECIPE BOOK!')

    logged_in = user_login()


    while True:
        print(f'There Are Currently {len(recipes)} recipes')
        if logged_in:
            print('You are currently Logged In')
        else:
            print('You are not Logged In')
        print("""
Please enter your desired option
0. Exit
1. Search for a Recipe
2. Add a New Recipe
3. Make changes to existing Recipe (Edit)
4. Delete Recipe
    """)
        if logged_in:
            print('5. Log Out')
        else:
            print('5. Log In')
        user_input = get_number_input(0, 5)
        if not logged_in and user_input > 1 and user_input != 5:
            print('Sorry, you do not have access. Only premium users can enjoy this feature.\n')

        elif user_input == 0:
            print('Thanks for your time. Bye!')
            break
        elif user_input == 1:
            print("""
Please enter your desired option:
Do you want to search by 
1. Food Name 
2. Ingredients\n""")
            search_term = get_number_input(1, 2)
            if search_term == 1:
                selected_recipe = recipe_search(recipes)
            elif search_term == 2:
                selected_recipe = recipe_search_ingredients(recipes)
            if selected_recipe:
                display_recipe(selected_recipe)
        elif user_input == 2:
            new_recipe = create_recipe()
            recipes.append(new_recipe)
            save_recipes(recipes)
        elif user_input == 3:
            edit_recipe(recipes)
        elif user_input == 4:
            delete_recipe(recipes)
        elif user_input == 5:
            if logged_in:
                logged_in = False
                print('You have been logged out!')
            else:
                logged_in = user_login()


# convert python data structure into JSON string

def user_login():
    print('You can log in to access premium features')
    login = yes_no('Do you want to log in?\n')
    if login:
        user_name = get_string('Please enter your name:\n')
        #TODO: Display **** when typing the password
        password = getpass.getpass(prompt='Please enter your password')
        hashes = load_users()
        pwd_context = CryptContext(
            schemes=["pbkdf2_sha256"],
            default="pbkdf2_sha256",
            pbkdf2_sha256__default_rounds=30000
        )
        if not user_name in hashes:
            print('Username not found')
        else:
            user_hash = hashes[user_name]
            if pwd_context.verify(password, user_hash):
                print("You're Logged in")
                return True
            else:
                print('Password incorrect')
    else:
        print('You will have limited features\n')
    return False

def load_users():
    f = open('users.json', 'r')
    users_string = f.read()
    f.close()
    return json.loads(users_string)


def save_recipes(recipes):
    json_string = json.dumps(recipes)
    f = open(recipes_filepath(), 'w')
    f.write(json_string)
    f.close()


def load_recipes():
    f = open(recipes_filepath(), 'r')
    recipes_string = f.read()
    f.close()
    return json.loads(recipes_string)

def recipes_filepath():
    if __name__ == '__main__':
        return 'recipes.json'
    else:
        return 'test_recipes.json'


def display_recipe(recipe):
    recipe_name = recipe['name'].upper()
    print(f'How to cook {recipe_name}')
    print('Ingredients:')
    for i, ingredient in enumerate(recipe['ingredients']):
        name = ingredient[0]
        amount = ingredient[1]
        print(f'{i + 1}.  {name}, {amount}')
    print('Instructions:')
    step_n = 1
    for step in recipe['instructions']:
        print(f'  {step_n}: {step}')
        step_n += 1


def create_recipe():
    recipe = {}
    name_food = get_string('What food do you want to add to the recipe book?\n'.capitalize())
    recipe['name'] = name_food

    ingredients = []
    while True:
        ingredient_name = get_string('Please Enter Name of Ingredient, or "done" if you are finished:\n')
        if ingredient_name == 'done':
            print(ingredients)
            break
        else:
            ingredient_amount = get_string(f'Please Enter Amount of {ingredient_name}:\n')
            ingredient = [ingredient_name, ingredient_amount]
            ingredients.append(ingredient)
            print(f'Added {ingredient_name}, {ingredient_amount}')
    recipe['ingredients'] = ingredients

    instructions = []
    while True:
        instruction = get_string(f'Please Enter Instruction {len(instructions) + 1}, or "done" if you are finished:\n')
        if instruction == 'done':
            print(instructions)
            break
        else:
            instructions.append(instruction)
    recipe['instructions'] = instructions

    return recipe



def edit_recipe_instructions():
    global selected_recipe
    while True:
        print("""
    Please enter your desired option
    0. Done
    1. Add to existing instructions
    2. Edit
    3. Re-arrange instructions (Moving)
    4. Delete
        """)
        user_input = get_number_input(0, 4)
        instructions = selected_recipe['instructions']
        if user_input == 0:
            break
        elif user_input == 1:
            add_instructions(selected_recipe)
            break
        elif user_input == 2:
            print('Enter the number of the instruction you want to edit:\n')
            edit_instruction_num = get_number_input(1, len(instructions))
            edit_instruction = get_string('Re-enter the instruction here to edit:\n')
            del instructions[edit_instruction_num - 1]
            instructions.insert(edit_instruction_num - 1, edit_instruction)
            break
        elif user_input == 3:
            move_instruction(selected_recipe)
            break
        elif user_input == 4:
            print('Enter the number of the instruction you want to delete:\n')
            delete_num = get_number_input(1, len(instructions))
            del instructions[delete_num - 1]
            print('Instruction Deleted!')



def edit_recipe_ingredients():
    global selected_recipe

    while True:
        print("""
    Please enter your desired option
    0. Done
    1. Add to existing ingredients
    2. Edit
    3. Delete
        """)
        user_input = get_number_input(0, 3)
        ingredients = selected_recipe['ingredients']
        if user_input == 0:
            break
        elif user_input == 1:
            add_ingredients(selected_recipe)
            break
        elif user_input == 2:
            edit_ingredients(ingredients)
            break
        elif user_input == 3:
            print('Enter the number of the ingredient you want to delete:\n')
            del_num = get_number_input(1, len(ingredients))
            del ingredients[del_num - 1]
            print('Ingredients Deleted!')


def edit_recipe(recipes):
    global selected_recipe
    selected_recipe = recipe_search(recipes)
    if selected_recipe:
        print(f'These are the details of your choice:')
        display_recipe(selected_recipe)
        name_answer = yes_no("""Do you want to make changes to the name of the food you selected?
        \nPlease input Yes(y) or No(n): """)
        if not name_answer:
            print(f"Great! The food name: {selected_recipe['name']} is maintained!")
        else:
            edit_name = input('Enter a new name for the food you are updating:\n').strip()
            if edit_name == '':
                print('Great! The name is unchanged')
            else:
                selected_recipe['name'] = edit_name
                print('The recipe name has been changed')
        ingredient_answer = yes_no("""Do you want to make changes to the ingredients of the food you selected?
                        \nPlease input Yes(y) or No(n): """)
        if not ingredient_answer:
            print(f"Great! The ingredients are  maintained!")
        else:
            edit_recipe_ingredients()
        save_recipes(recipes)
        instruction_answer = yes_no("""Do you want to make changes to the instructions of the food you selected?
        \nPlease input Yes(y) or No(n): """)
        if not instruction_answer:
            print(f"Great! The instructions are  maintained!")
        else:
            edit_recipe_instructions()
        save_recipes(recipes)
        display_recipe(selected_recipe)
    else:
        print('Returning to Main Menu')


def delete_recipe(recipes):
    selected_recipe = recipe_search(recipes)
    print(selected_recipe)
    if selected_recipe:
        print(f'These are the details of your choice:')
        display_recipe(selected_recipe)
        delete_answer = yes_no("""Are you sure you want to DELETE this recipe?
        \nPlease input Yes(y) or No(n): """)
        if not delete_answer:
            print(f"Great! The recipe for: {selected_recipe['name']} is maintained!")
        else:
            recipes.remove(selected_recipe)
            print(recipes)
        save_recipes(recipes)
        print('Recipe Deleted!')
    else:
        print('Delete Canceled!')



if __name__ == '__main__':
    main()

