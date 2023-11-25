import logging

# Setting up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class Product:  # Clear class name
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Include Units in Variable Names, Be Cautious with Naming Conventions
class Order:  # Clear class name
    def __init__(self, product, quantity, tax_rate, shipping_cost):
        self.product = product
        self.quantity = quantity
        self.tax_rate = tax_rate  # Clear unit indication
        self.shipping_cost = shipping_cost

    def calculate_total(self):
        total_cost = self.product.price * self.quantity
        total_cost += total_cost * self.tax_rate
        total_cost += self.shipping_cost
        return total_cost

# Rethink Naming if Struggling, Organize Code Logically
def calculate_order_total(product, quantity, tax_rate, shipping_cost):  # Descriptive function name
    return product.price * quantity + product.price * quantity * tax_rate + shipping_cost

# Testing with assert
def test_order_calculation():
    apples = Product("Apples", 20.0)  # Descriptive variable name
    order = Order(apples, 3, 0.05, 5.0)  # Descriptive variable name
    assert order.calculate_total() == 68.0, "Order total calculation error"
    assert calculate_order_total(apples, 5, 0.05, 5.0) == 110.0, "Order total utility calculation error"
    logging.info("All tests passed for order calculation!")

test_order_calculation()
