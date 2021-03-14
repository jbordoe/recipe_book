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

    def test_edit_ingredient(self):  # editing the both name and amount of ingredient only
        my_recipe = Recipe('Chicken Sandwich', [['chicken', '100g']], ["blah blah"])
        my_recipe.edit_ingredient(1, name='bread', amount='25g')
        self.assertEqual(my_recipe.ingredients, [['bread', '25g']])


        # editing the name of ingredient only
        my_recipe = Recipe('Chicken Sandwich', [['chicken', '100g']], ["blah blah"])
        my_recipe.edit_ingredient(1, name='pepper')
        self.assertEqual(my_recipe.ingredients, [['pepper', '100g']])

        # editing the amount of the ingredient
        my_recipe = Recipe('Chicken Sandwich', [['chicken', '100g'], ['tomatoes', '5g']], ["blah blah"])
        my_recipe.edit_ingredient(2, amount='30g')
        self.assertEqual(my_recipe.ingredients, [['chicken', '100g'], ['tomatoes', '30g']])


    def test_add_instruction(self):
        my_recipe = Recipe('Chicken Sandwich', [], [])
        my_recipe.add_instruction(1, "blah blah blah")
        self.assertEqual(my_recipe.instructions, ['blah blah blah'])

        my_recipe = Recipe('Chicken Sandwich', [], ["blah blah blah"])
        my_recipe.add_instruction(5, "ha ha ha")
        self.assertEqual(my_recipe.instructions, ['blah blah blah', 'ha ha ha'])

        my_recipe = Recipe('Chicken Sandwich', [], ['a', 'b', 'c'])
        my_recipe.add_instruction(1, "ha ha ha")
        self.assertEqual(my_recipe.instructions, ["ha ha ha", 'a', 'b', 'c'])

        my_recipe = Recipe('Chicken Sandwich', [], ['a', 'b', 'c'])
        my_recipe.add_instruction(2, "ha ha ha")
        self.assertEqual(my_recipe.instructions, ['a', "ha ha ha", 'b', 'c'])

    def test_move_instruction(self):
        my_recipe = Recipe('Chicken Sandwich', [], ['a', 'b', 'c'])
        my_recipe.move_instruction(2, 3)
        self.assertEqual(my_recipe.instructions, ['a', 'c', 'b'])

        my_recipe = Recipe('Chicken Sandwich', [], ['a', 'b', 'c'])
        my_recipe.move_instruction(3, 3)
        self.assertEqual(my_recipe.instructions, ['a', 'b', 'c'])

        my_recipe = Recipe('Chicken Sandwich', [], ['a', 'b', 'c'])
        my_recipe.move_instruction(1, 10)
        self.assertEqual(my_recipe.instructions, ['b', 'c', 'a'])

    def test_edit_instruction(self):
        my_recipe = Recipe('Chicken Sandwich', [], ['a', 'b', 'c'])
        my_recipe.edit_instruction(2, 'j')
        self.assertEqual(my_recipe.instructions, ['a', 'j', 'c'])


# TODO: throw an error if the old position is too large or too small


if __name__ == '__main__':
    unittest.main()
