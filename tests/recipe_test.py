import unittest
from recipe import Recipe


class RecipeTest(unittest.TestCase):
    def test_constructor(self):
        my_recipe = Recipe('Chicken Sandwich', [['chicken', 'bread']], ["blah blah"])

        self.assertEqual(my_recipe.name, 'Chicken Sandwich')
        self.assertEqual(my_recipe.ingredients, [['chicken', 'bread']])
        self.assertEqual(my_recipe.instructions, ["blah blah"])

    def test_add_ingredient(self):
        my_recipe = Recipe('Chicken Sandwich', [['chicken', '100g']], ["blah blah"])
        my_recipe.add_ingredient('pepper', '4')
        self.assertEqual(my_recipe.ingredients, [['chicken', '100g'], ['pepper', '4']])


if __name__ == '__main__':
    unittest.main()
