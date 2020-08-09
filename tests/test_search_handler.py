import unittest
from unittest.mock import patch
from search_handler import recipe_search, recipe_search_ingredients


class SearchHandlerTest(unittest.TestCase):
    def test_recipe_search(self):
        recipes = [{'name': 'Gari'},
                   {'name': 'Banku'},
                   {'name': 'Jolof Rice'},
                   {'name': 'Waakye'},
                   {'name': 'Rice Balls'}]
        #Even search is successful
        search_term = 'rice'
        selection = '2'
        with patch('builtins.input', side_effect=[search_term, selection]) as m:
            selected = recipe_search(recipes)
            self.assertEqual({'name': 'Rice Balls'}, selected)


        #Even search is unsuccessful
        search_term = 'Potatoes'
        selection = 'no'
        with patch('builtins.input', side_effect=[search_term, selection]) as m:
            selected = recipe_search(recipes)
            self.assertEqual(False, selected)


        #User cancels after a successful search
        search_term = 'Rice'
        selection = '0'
        with patch('builtins.input', side_effect=[search_term, selection]) as m:
            selected = recipe_search(recipes)
            self.assertEqual(False, selected)


    def test_recipe_search_ingredients(self):
        recipes = [{'name': 'TZ', 'ingredients': [['corn dough', '50g'], ['millet', '100']]},
                   {'name': 'banku', 'ingredients': [['corn dough', '50g'], ['cassava dough', '100']]},
                   {'name': 'fufu', 'ingredients': [['plantain', '800g'], ['cocoyam', '100']]}]

        # Even search is successful with ingredients
        search_term = 'corn dough'
        selection = '1'
        with patch('builtins.input', side_effect=[search_term, selection]) as m:
            selected = recipe_search_ingredients(recipes)
            self.assertEqual(recipes[0], selected)

        # Even search is unsuccessful with ingredients
        search_term = 'Potatoes'
        selection = 'no'
        with patch('builtins.input', side_effect=[search_term, selection]) as m:
            selected = recipe_search_ingredients(recipes)
            self.assertEqual(False, selected)

        # User cancels after a successful search
        search_term = 'plantain'
        selection = '0'
        with patch('builtins.input', side_effect=[search_term, selection]) as m:
            selected = recipe_search_ingredients(recipes)
            self.assertEqual(False, selected)


if __name__ == '__main__':
    unittest.main()
