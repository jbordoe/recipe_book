import unittest
from unittest.mock import patch
from main import create_recipe, delete_recipe, edit_recipe


class MainTestCase(unittest.TestCase):
    def test_create_recipe(self):
        #Create a recipe that has only a name
        with patch('builtins.input', side_effect=['banku', 'done', 'done']) as m:
            recipe = create_recipe()
            self.assertEqual({'name': 'banku', 'ingredients': [], 'instructions': []}, recipe)

        #Adding ingredients to the new recipe
        with patch('builtins.input', side_effect=['banku', 'pepper', '50g', 'done', 'done']) as m:
            recipe = create_recipe()
            self.assertEqual({'name': 'banku', 'ingredients': [['pepper', '50g']], 'instructions': []}, recipe)

        #Adding instructions to the new recipe
        with patch('builtins.input', side_effect=['banku', 'pepper', '50g', 'done', 'Boil the cassava and plantain', 'done']) as m:
            recipe = create_recipe()
            self.assertEqual({'name': 'banku', 'ingredients': [['pepper', '50g']], 'instructions': ["Boil the cassava and plantain"]}, recipe)


    def test_delete_recipe(self):
        #Deleting recipes
        recipes = [{'name': 'Gari'},
                   {'name': 'Banku'},
                   {'name': 'Jolof Rice', 'ingredients': [], 'instructions': []},
                   {'name': 'Waakye'},
                   {'name': 'Rice Balls'}]
        with patch('builtins.input', side_effect=['Rice', '1', 'Yes']) as n:
            delete_recipe(recipes)
            self.assertEqual([{'name': 'Gari'}, {'name': 'Banku'}, {'name': 'Waakye'}, {'name': 'Rice Balls'}], recipes)

        #Not Deleting recipe
        recipes = [{'name': 'Gari'},
                   {'name': 'Banku'},
                   {'name': 'Jolof Rice', 'ingredients': [], 'instructions': []},
                   {'name': 'Waakye'},
                   {'name': 'Rice Balls'}]
        with patch('builtins.input', side_effect=['Rice', '1', 'No']) as n:
            delete_recipe(recipes)
            self.assertEqual([{'name': 'Gari'},
                              {'name': 'Banku'},
                              {'name': 'Jolof Rice', 'ingredients': [], 'instructions': []},
                              {'name': 'Waakye'},
                              {'name': 'Rice Balls'}], recipes)


    def test_edit_recipe(self):
            #Editing recipes name only
        recipes = [{'name': 'Gari'},
                       {'name': 'Banku', 'ingredients': [], 'instructions': []},
                       {'name': 'Waakye'},
                       {'name': 'Rice Balls'}]
        with patch('builtins.input', side_effect=['Banku', '1', 'Yes', 'TZ', 'No', 'No']) as n:
            edit_recipe(recipes)
            self.assertEqual([{'name': 'Gari'}, {'name': 'TZ', 'ingredients': [], 'instructions': []},
                              {'name': 'Waakye'}, {'name': 'Rice Balls'}], recipes)


            #Editing recipes name and ingredients only
        recipes = [{'name': 'Gari'},
                       {'name': 'Banku', 'ingredients': [['pepper', '20g']], 'instructions': []},
                       {'name': 'Waakye'},
                       {'name': 'Rice Balls'}]
        with patch('builtins.input', side_effect=['Banku', '1', 'Yes', 'TZ', 'Yes', '2', '1', 'tomatoes', '',
                                                  'No', '0', 'No']) as n:
            edit_recipe(recipes)
            self.assertEqual([{'name': 'Gari'}, {'name': 'TZ', 'ingredients': [['tomatoes', '20g']], 'instructions': []},
                              {'name': 'Waakye'}, {'name': 'Rice Balls'}], recipes)


        #Editing recipes name, ingredients and instructions (adding)
        recipes = [{'name': 'Gari'},
                   {'name': 'Banku', 'ingredients': [['pepper', '20g']], 'instructions': ['prepare the corn dough']},
                   {'name': 'Waakye'},
                   {'name': 'Rice Balls'}]
        with patch('builtins.input', side_effect=['Banku', '1', 'Yes', 'TZ', 'Yes', '2', '1', 'tomatoes', '',
                                                  'No', '0', 'Yes', '1', 'prepare the cassava dough', '1', 'No']) as n:

            edit_recipe(recipes)
            self.assertEqual(
                [{'name': 'Gari'}, {'name': 'TZ', 'ingredients': [['tomatoes', '20g']],
                                    'instructions': ['prepare the cassava dough', 'prepare the corn dough']},
                 {'name': 'Waakye'}, {'name': 'Rice Balls'}], recipes)


if __name__ == '__main__':
    unittest.main()
