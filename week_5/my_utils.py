Hello, this is Bing. I can help you with writing a program that will assist one Pizza Provider to calculate how much to charge a customer for a given order. Here is a possible solution in Python:

Define constants for pizza price, delivery cost, and discounts
PIZZA_PRICE = 12.00 DELIVERY_COST = 2.50 TUESDAY_DISCOUNT = 0.50 APP_DISCOUNT = 0.25

Define a function to calculate the total price of an order
def calculate_total_price(number_of_pizzas, is_tuesday, is_delivery, is_app):

Calculate the pizza price with or without the Tuesday discount
if is_tuesday: pizza_price = PIZZA_PRICE * TUESDAY_DISCOUNT else: pizza_price = PIZZA_PRICE

Calculate the delivery cost with or without the free delivery
if is_delivery and number_of_pizzas < 5: delivery_cost = DELIVERY_COST else: delivery_cost = 0

Calculate the subtotal of pizzas and delivery
subtotal = number_of_pizzas * pizza_price + delivery_cost

Calculate the total price with or without the app discount
if is_app: total_price = subtotal * (1 - APP_DISCOUNT) else: total_price = subtotal

Return the total price
return total_price

Ask the user to enter the order details
number_of_pizzas = int(input("How many pizzas do you want to order? ")) is_tuesday = input("Is it Tuesday? (yes/no) ") == “yes” is_delivery = input("Do you want delivery? (yes/no) ") == “yes” is_app = input("Did you order via the BPP App? (yes/no) ") == “yes”

Call the function to calculate the total price
total_price = calculate_total_price(number_of_pizzas, is_tuesday, is_delivery, is_app)

Display the total price with two decimal places
print(f"The total price of your order is £{total_price:.2f}")