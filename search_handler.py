from input_handler import get_number_input, yes_no


def recipe_search_menu(recipes):
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
        return selected_recipe

def recipe_search(recipes):
    while True:
        query = input('Enter your search term: ').strip()
        if query == '':
            print('Search canceled')
            break
        matches = find_recipe_by_name(recipes, query)
        print(f'Found {len(matches)} match(es)!')

        if len(matches) == 0:
            if yes_no('Do you want to try a new search? '):
                continue
            else:
                return False

        names = list(map(lambda x: x['name'], matches))

        print('0. Return to Main Menu')
        for i in range(0, len(names)):
            print(f'{i + 1}. {names[i]}\n')

        print('Enter a number related to the food (match) you are interested: ')
        num_input = get_number_input(0, len(matches))
        if num_input == 0:
            print('Returning to main menu')
            return False
        else:
            selected_recipe = matches[num_input - 1]
            return selected_recipe

def find_recipe_by_name(recipes, query):
    return list(filter(lambda x: query.lower() in x['name'].lower(), recipes))

def recipe_search_ingredients(recipes):
    while True:
        query = input('Enter your search term by ingredient: ').strip()
        if query == '':
            print('Search canceled')
            break
        matches = []
        for recipe in recipes:
            for ingredient in recipe['ingredients']:
                ingredient_name = ingredient[0]
                if query.lower() in ingredient_name:
                    matches.append(recipe)

        print(f'Found {len(matches)} match(es)!')

        if len(matches) == 0:
            if yes_no('Do you want to try a new search? '):
                continue
            else:
                return False
        food_ingredients = list(map(lambda x: x['name'], matches))

        print('0. Return to Main Menu')
        for i in range(0, len(food_ingredients)):
            print(f'{i + 1}. {food_ingredients[i]}\n')

        print('Enter a number related to the food (match) you are interested: ')
        num_input = get_number_input(0, len(matches))
        if num_input == 0:
            print('Returning to main menu')
            return False
        else:
            selected_recipe = matches[num_input - 1]
            return selected_recipe


