
def log_decorator(func):

    def wrapper(*args, **kwargs):
        product_id = args[1]
        print(f"Logging product operation for product id: {product_id} ")
        return func(*args, **kwargs)

    return wrapper


class ProductManagement:

    @log_decorator
    def add_product(self, product_id, name):
        # add product ot database
        print(f"adding product {name} with id {product_id}")

    @log_decorator
    def update_product(self, product_id):
        print(f"updating product id {product_id}")

    @log_decorator
    def delete_product(self, product_id):
        print(f"deleting product with id: {product_id}")


# Usage
product_management = ProductManagement()
product_management.add_product(123, "Product A")
product_management.delete_product(124)
