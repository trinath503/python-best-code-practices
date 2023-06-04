class InventoryTracker:

    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, item_quantity):
        self.inventory[item_name] = item_quantity

    def track_inventory(self):
        for item_name, item_quantity in self.inventory.items():
            yield f"{item_name}: {item_quantity} in stock"

    def get_inventory(self, page_size=10):
        num_of_pages = (len(self.inventory) + page_size - 1) // page_size
        for page in range(num_of_pages):
            start_page = page * page_size
            end_page = start_page + page_size
            yield list(self.inventory.items())[start_page:end_page]

# Usage


inventory_tracker = InventoryTracker()
inventory_tracker.add_item("Product A", 10)
inventory_tracker.add_item("Product B", 5)

inventory_generator = inventory_tracker.track_inventory()
for item in inventory_generator:
    print(item)

inventory_page_generator = inventory_tracker.get_inventory()
for items in inventory_page_generator:
    for item in items:
        print(item)
