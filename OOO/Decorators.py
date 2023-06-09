# function that takes another function and extends the behavior of the latter function without explicitly modifying it
# design pattern that allows you to modify the functionality of a function by wrapping it in another function.

# Example -1:
def sum_decorator(func):
    def wrapper(a,b, *args, **kwargs):
        print('wrapper')
        # print(args[0],args[1], args, kwargs)
        print(a,b, args, kwargs)
        return func(a,b) 

    return wrapper
@sum_decorator
def sum_of_two_numbers(a,b):
    print('sum_of_two_numbers')
    return a+b

for numbers in [[1,2, 3], [3,4, 7]]:
    print('numbers:')
    print(sum_of_two_numbers(numbers[0], numbers[1], numbers[2]))



# Example -2:
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
