"""
Sure! The SOLID principles are a set of design principles that help create maintainable and scalable software. Let's explore each principle with real-world examples in the context of a retail application.

1. Single Responsibility Principle (SRP):
   The SRP states that a class should have only one reason to change. It should have a single responsibility and should be focused on doing one thing well.

   Example: `ProductCatalog` class

   The `ProductCatalog` class is responsible for managing and providing access to product data. Its single responsibility is to handle product-related operations, such as adding products, retrieving product information, or generating product recommendations. By adhering to the SRP, the `ProductCatalog` class remains focused on its specific domain and is less prone to changes caused by unrelated functionalities.

2. Open-Closed Principle (OCP):
   The OCP states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. It promotes the idea that existing code should not be modified when new functionalities are added but rather extended through well-defined interfaces or abstractions.

   Example: `DiscountCalculator` class

   The `DiscountCalculator` class calculates discounts for products based on different criteria, such as membership status, purchase history, or promotional campaigns. By adhering to the OCP, the class can be easily extended to support new discount calculation strategies without modifying the existing code. New discount calculation methods can be implemented by creating subclasses or implementing interfaces and injecting them into the `DiscountCalculator` class.

3. Liskov Substitution Principle (LSP):
   The LSP states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program. It ensures that inheritance hierarchies are well-designed and follow the "is-a" relationship.

   Example: `PaymentProcessor` class

   The `PaymentProcessor` class handles payment processing for various payment methods such as credit cards, e-wallets, or gift cards. It provides a common interface for processing payments. By adhering to the LSP, any subclass that implements the `PaymentProcessor` interface can be used interchangeably without impacting the overall functionality. For example, a new subclass for processing cryptocurrency payments can be added without affecting the existing code that relies on the `PaymentProcessor` interface.

4. Interface Segregation Principle (ISP):
   The ISP states that clients should not be forced to depend on interfaces they do not use. It promotes the idea of segregating interfaces into smaller, more focused ones to avoid unnecessary dependencies and to provide clients with only the methods they require.

   Example: `OrderProcessor` class

   The `OrderProcessor` class handles the processing of incoming orders, which includes validating orders, calculating order totals, and updating inventory. By adhering to the ISP, the `OrderProcessor` class can implement multiple interfaces, each catering to a specific aspect of order processing. For instance, it can implement `OrderValidation`, `OrderTotalCalculation`, and `InventoryUpdater` interfaces, allowing clients to depend only on the interfaces they need.

5. Dependency Inversion Principle (DIP):
   The DIP states that high-level modules should not depend on low-level modules. Both should depend on abstractions. It promotes loose coupling between modules and enables flexibility and easier testing by relying on abstractions rather than concrete implementations.

   Example: `OrderManagement` class

   The `OrderManagement` class is responsible for managing and processing orders. By adhering to the DIP, the class depends on abstractions, such as interfaces or abstract classes, rather than concrete implementations of dependencies like `PaymentProcessor` or `InventoryTracker`. This allows for easier swapping of different implementations or mocking dependencies during testing, as well as making the system more

 extensible by supporting new implementations without modifying the `OrderManagement` class.

By following these SOLID principles, the retail application can achieve code that is more modular, flexible, and easier to maintain and extend over time. These principles promote good design practices that result in software that is more robust, reusable, and adaptable to changes in requirements.



"""


# 1. Single Responsibility


class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_product(self, product_id):
        for product in self.products:
            if product["id"] == product_id:
                return product

    def generate_recommendations(self):
        # Generate product recommendations based on certain criteria
        pass


# 2. Open - Closed


class DiscountCalculator:
    def calculate_discount(self, product):
        # Calculate discount based on specific rules
        pass


class PercentageDiscountCalculator(DiscountCalculator):
    def calculate_discount(self, product):
        # Calculate discount as a percentage of the product price
        pass


class FixedAmountDiscountCalculator(DiscountCalculator):
    def calculate_discount(self, product):
        # Calculate discount as a fixed amount
        pass


# 3. Liskov Substitution


class PaymentProcessor:
    def process_payment(self, amount):
        # Process payment for the given amount
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Process credit card payment for the given amount
        pass


class EWalletPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        # Process e-wallet payment for the given amount
        pass


# 4 Interface Segregation Principle


class OrderValidation:
    def validate_order(self, order):
        # Validate the order
        pass


class OrderTotalCalculation:
    def calculate_order_total(self, order):
        # Calculate the total amount of the order
        pass


class InventoryUpdater:
    def update_inventory(self, order):
        # Update the inventory based on the order
        pass


class OrderProcessor(OrderValidation, OrderTotalCalculation, InventoryUpdater):
    def process_order(self, order):
        self.validate_order(order)
        total = self.calculate_order_total(order)
        self.update_inventory(order)
        # Other order processing logic


# 5.Dependency Inversion Principle (DIP)


class OrderManagement:

    def __init__(self, payment_processor, inventory_tracker):
        self.payment_processor = payment_processor
        self.inventory_tracker = inventory_tracker

    def process_order(self, order):
        # Perform order processing logic
        payment_status = self.payment_processor.process_payment(order.total_amount)
        if payment_status == "success":
            self.inventory_tracker.update_inventory(order)
            # Other order processing steps


payment_processor = CreditCardPaymentProcessor()
inventory_tracker = DatabaseInventoryTracker()
order_management = OrderManagement(payment_processor, inventory_tracker)
