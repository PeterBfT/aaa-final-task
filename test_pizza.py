import pizza
from unittest.mock import patch
from click.testing import CliRunner


class TestPizza:
    """Класс для тестирования программы pizza.py"""

    @patch('builtins.print')
    def test_dict(self, mock_print):
        """Тестирование функции dict в классе PizzaRecipe"""
        pizza_example = pizza.PizzaRecipe('Ananasovaya', 'ananas', 'pizza')
        pizza_example.dict()
        mock_print.assert_called_with('Ananasovaya: ananas, pizza')

    @patch('builtins.print')
    def test_big_pizza(self, mock_print):
        """Тестирование функции big_pizza в классе CookingPizza"""
        pizza_cooking_example = pizza.CookingPizza()
        pizza_cooking_example.big_pizza()
        mock_print.assert_called_with('😎 Большая пицца')

    @patch('pizza.randint')
    def test_order_no_delivery_no_size(self, mock_randint):
        """
        Тестирование команды order,
        Подается на вход только название пиццы из списка
        """
        mock_randint.return_value = 25
        result = CliRunner().invoke(pizza.order, ['margherita'])
        exp_result = '👨‍🍳 Приготовили за 25с!\n🏠 Забрали за 25с!\n'
        assert result.output == exp_result

    @patch('pizza.randint')
    def test_order_delivery(self, mock_randint):
        """
        Тестирование команды order,
        Подается на вход название пиццы из списка и флаг доставки
        """
        mock_randint.return_value = 25
        result = CliRunner().invoke(pizza.order, ['margherita', '--delivery'])
        exp_result = '👨‍🍳 Приготовили за 25с!\n🛵 Доставили за 25с!\n'
        assert result.output == exp_result

    @patch('pizza.randint')
    def test_order_size(self, mock_randint):
        """
        Тестирование команды order,
        Подается на вход название пиццы и флаг размера пиццы со значением XL
        """
        mock_randint.return_value = 25
        result = CliRunner().invoke(pizza.order, ['margherita', '--size=xL'])
        exp_result_ar = [
            '😎 Большая пицца\n',
            '👨‍🍳 Приготовили за 25с!\n',
            '🏠 Забрали за 25с!\n'
        ]
        exp_result = ''.join(exp_result_ar)
        assert result.output == exp_result

    def test_order_wrong_pizza(self):
        """
        Тестирование команды order,
        Подается на вход название пиццы, которого нет в меню
        """
        result = CliRunner().invoke(pizza.order, ['Ananasovaya'])
        exp_result = 'Такой пиццы пока нет в нашем меню\n'
        assert result.output == exp_result

    def test_menu(self):
        """Тестирование команды menu"""
        runner = CliRunner()
        result = runner.invoke(pizza.menu)
        exp_result_ar = [
            '- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n',
            '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n',
            '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'
        ]
        exp_result = ''.join(exp_result_ar)
        assert result.output == exp_result
