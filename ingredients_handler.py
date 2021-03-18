from input_handler import get_string, get_number_input, yes_no


def add_ingredients(selected_recipe):
    ingredients = selected_recipe['ingredients']
    while True:
        add_ingredient = get_string('Enter the name of the ingredients:\n')
        amount_ingredients = get_string('Enter the amount of ingredient:\n')
        add_amt_ingredient = [add_ingredient, amount_ingredients]
        ingredients.append(add_amt_ingredient)
        print('Added Ingredients')
        ingre_ans = yes_no("""Do you want to add another ingredient?
                        \nPlease input Yes(y) or No(n): """)
        if not ingre_ans:
            break
#TODO: Separate user input and data manipulation functions

def edit_ingredients(ingredients):
    while True:
        print('Enter the number of the ingredient you want to edit:\n')
        edit_ingredients_num = get_number_input(1, len(ingredients))

        new_ingredients = input('Enter the name of the ingredients:\n').strip()
        if new_ingredients == '':
            new_ingredients = ingredients[edit_ingredients_num - 1][0]
            print('Ingredient name unchanged!')
        amount_ingredients = input('Enter the amount of ingredient:\n').strip()
        if amount_ingredients == '':
            amount_ingredients = ingredients[edit_ingredients_num - 1][1]
            print('Ingredient amount unchanged!')
        add_amt_ingredient = [new_ingredients, amount_ingredients]
        del ingredients[edit_ingredients_num - 1]
        ingredients.append(add_amt_ingredient)
        edit_ingredient_ans = yes_no("""Do you want to edit another ingredient?
                                \nPlease input Yes(y) or No(n): """)
        if not edit_ingredient_ans:
            break
