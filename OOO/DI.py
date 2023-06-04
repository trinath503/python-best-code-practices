"""
    There are 3 types of dependency injection
        - constructor
        - settor
        - method

"""

# 1. Constructor


class EmailService:

    def send_email(self, recipient, message ):
        return f" Sending email to {recipient} : {message}"


class NotificationService:

    def __init__(self, email_service):
        self.email_service = email_service

    def send_notification(self, recipient, message):
        self.email_service.send_email(recipient, message)


email_service = EmailService()
notfication_service = NotificationService(email_service)
notfication_service.send_notification("username@gmail.com", "message")

# Service with Multiple Dependencies


class Logger:

    def __init__(self):
        self.logs = []

    def log(self, message):
        print(f"{message}")
        self.logs.append(message)


class DataBase:

    def __init__(self, connection_config):
        self.connection_config = connection_config

    def connect(self):
        print(f"Connected to database : {self.connection_config}")


class ProductService:

    def __init__(self, database: DataBase, logger: Logger):
        self.database = database
        self.logger = logger

    def save_product(self, product):
        self.database.connect()
        self.logger.log(f" added product to inventory: {product}")


database = DataBase("mysql://localhost:3306/products/")
logger = Logger()
product_service  = ProductService(database, logger)
product_service.save_product({"name": "Product1"})

#####################################################
#           2. Setter/Property                      #
#####################################################


class CategoryService:
    def get_category(self, category_id):
        # Retrieve category information from database
        return {"id": category_id, "name": "Electronics"}


class ProductCatalog:
    def set_category_service(self, category_service):
        self.category_service = category_service

    def get_product(self, product_id):
        # Retrieve product information from database
        category_id = 123
        category = self.category_service.get_category(category_id)
        return {"id": product_id, "name": "Smartphone", "category": category}

# Usage
category_service = CategoryService()
product_catalog = ProductCatalog()
product_catalog.set_category_service(category_service)
product = product_catalog.get_product(456)
print(product)

# example -2


class PaymentGateway:
    def process_payment(self, order, amount):
        # Process payment using a payment gateway API
        return "Payment successful"


class OrderManagement:
    def set_payment_gateway(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def place_order(self, order):
        # Calculate order total
        amount = 100
        result = self.payment_gateway.process_payment(order, amount)
        if result == "Payment successful":
            # Proceed with order placement
            pass

# Usage
payment_gateway = PaymentGateway()
order_management = OrderManagement()
order_management.set_payment_gateway(payment_gateway)
order = {"id": 123, "items": [...] }
order_management.place_order(order)

#####################################################
#           3. Method Injection                     #
#####################################################

class CustomerService:
    def get_customer_profile(self, customer_id):
        # Retrieve customer profile from database
        return {"id": customer_id, "name": "John Doe", "age": 30}

class ProductRecommendation:
    def recommend_products(self, customer_id):
        # Retrieve customer profile
        customer_service = CustomerService()
        customer_profile = customer_service.get_customer_profile(customer_id)

        # Perform recommendation logic based on customer profile
        recommended_products = [...]
        return recommended_products

# Usage
product_recommendation = ProductRecommendation()
recommended_products = product_recommendation.recommend_products(123)
print(recommended_products)



# example -2


class DiscountService:
    def calculate_discount(self, product):
        # Calculate discount based on product and user information
        return 0.1  # Return a discount of 10%

class PriceCalculator:
    def calculate_price(self, product_id):
        # Retrieve product information from database
        product = {"id": product_id, "name": "Product A", "price": 100}

        # Calculate discount
        discount_service = DiscountService()
        discount = discount_service.calculate_discount(product)

        # Apply discount to calculate the final price
        final_price = product["price"] * (1 - discount)
        return final_price

# Usage
price_calculator = PriceCalculator()
final_price = price_calculator.calculate_price(123)
print(final_price)
