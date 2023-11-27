import click
from random import randint


class PizzaRecipe:
    """Класс для создания рецепта пиццы"""

    def __init__(self, name: str, *args) -> None:
        """
        Создает пиццу

        Вход:
            name: название пиццы
            args: ингредиенты пиццы
        """
        self.name = name
        self.ingredients = [*args]

    def dict(self) -> None:
        """Выводит рецепт пиццы в виде словаря"""
        print('{}: {}'.format(self.name, ', '.join(self.ingredients)))


class CookingPizza:
    """Класс для готовки пиццы"""

    @staticmethod
    def log(string: str):
        """
        Декоратор для написания времени выполнения операции

        Вход:
            string: шаблон, в который подставляется время

        Время - рандомное натуральное число от 1 до 42,
        сгенерированное с помощью randint
        """
        def decorator(f):
            def wrapper(self):
                f(self)
                duration = randint(1, 42)
                print(string.format(duration))
            return wrapper
        return decorator

    @log('👨‍🍳 Приготовили за {}с!')
    def bake(self):
        """Готовит пиццу"""

    @log('🛵 Доставили за {}с!')
    def delivery(self):
        """Доставляет пиццу"""

    @log('🏠 Забрали за {}с!')
    def pickup(self):
        """Самовывоз"""

    def big_pizza(self):
        """Больщая пицца"""
        print('😎 Большая пицца')


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option(
    '--size', is_flag=False, flag_value='L', default='L',
    type=click.Choice(['L', 'XL'], case_sensitive=False)
)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool, size: str):
    """
    Готовит и доставляет пиццу

    Вход:
        name: название пиццы
        delivery: наличие доставки
        size: размер пиццы
    """

    pizzas = ['margherita', 'pepperoni', 'hawaiian']
    if pizza.lower() not in pizzas:
        print('Такой пиццы пока нет в нашем меню')
        return

    pizza_order = CookingPizza()

    if size == 'XL':
        pizza_order.big_pizza()

    pizza_order.bake()

    if delivery:
        pizza_order.delivery()
    else:
        pizza_order.pickup()


@cli.command()
def menu():
    """Выводит меню"""
    Margherita = PizzaRecipe('- Margherita 🧀', 'tomato sauce',
                             'mozzarella', 'tomatoes')
    Margherita.dict()

    Pepperoni = PizzaRecipe('- Pepperoni 🍕', 'tomato sauce',
                            'mozzarella', 'pepperoni')
    Pepperoni.dict()

    Hawaiian = PizzaRecipe('- Hawaiian 🍍', 'tomato sauce',
                           'mozzarella', 'chicken', 'pineapples')
    Hawaiian.dict()


if __name__ == '__main__':
    cli()
