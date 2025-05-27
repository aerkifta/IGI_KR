# pizza_app.py

class Pizza:
    BASE_PRICES = {'S': 5, 'M': 7, 'L': 9}
    TOPPING_PRICE = 0.5

    def __init__(self, name, size='M', toppings=None):
        self.name = name
        self.size = size.upper()
        self.toppings = toppings if toppings else []

    def price(self):
        base = self.BASE_PRICES.get(self.size, 7)
        return base + len(self.toppings) * self.TOPPING_PRICE

    def __str__(self):
        toppings = ', '.join(self.toppings) if self.toppings else 'без добавок'
        return f"{self.name} ({self.size}) [{toppings}] — {self.price():.2f} руб."


class Order:
    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def total_price(self):
        return sum(p.price() for p in self.pizzas)

    def summary(self):
        return '\n'.join(str(p) for p in self.pizzas) + \
               f"\nИтого: {self.total_price():.2f} руб."


class Terminal:
    def __init__(self):
        self.order = Order()

    def run(self):
        print("Добро пожаловать в пиццерию!")

        while True:
            name = input("Введите название пиццы (или 'стоп' для завершения): ")
            if name.lower() == 'стоп':
                break

            size = input("Размер пиццы (S/M/L): ").upper()
            toppings = input("Добавки через запятую (или Enter): ").split(',')
            toppings = [t.strip() for t in toppings if t.strip()]

            pizza = Pizza(name, size, toppings)
            self.order.add_pizza(pizza)
            print(f"Добавлена: {pizza}\n")

        print("\nВаш заказ:")
        print(self.order.summary())


if __name__ == "__main__":
    terminal = Terminal()
    terminal.run()
