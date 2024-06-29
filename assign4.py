#Ethan Thomas Davies Greene
#251348539
#egreene4
#December 08 2023

# Define a class representing a Product
class Product:
    def __init__(self, name, price, category):
        # Initialize product attributes
        self._name = name
        self._price = price
        self._category = category

    # Define how products are compared for equality
    def __eq__(self, other):
        if isinstance(other, Product):
            return (self._name == other._name and
                    self._price == other._price and
                    self._category == other._category)
        return False

    # Define the hash function for products
    def __hash__(self):
        return hash((self._name, self._price, self._category))

    # Getter methods for retrieving product attributes
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_category(self):
        return self._category

    # String representation of a Product
    def __repr__(self):
        rep = 'Product(' + self._name + ',' + str(self._price) + ',' + self._category + ')'
        return rep


# Define a class representing an Inventory
class Inventory:
    def __init__(self):
        # Initialize an empty dictionary to store products and their quantities
        self._products = {}

    # Method to add a product to the inventory
    def add_to_productInventory(self, productName, productPrice, productQuantity):
        self._products[productName] = {'price': productPrice, 'quantity': productQuantity}

    # Method to increase the quantity of a product in the inventory
    def add_productQuantity(self, nameProduct, addQuantity):
        if nameProduct in self._products:
            self._products[nameProduct]['quantity'] += addQuantity

    # Method to decrease the quantity of a product in the inventory
    def remove_productQuantity(self, nameProduct, removeQuantity):
        if nameProduct in self._products:
            if self._products[nameProduct]['quantity'] >= removeQuantity:
                self._products[nameProduct]['quantity'] -= removeQuantity

    # Getter methods to retrieve product price and quantity from the inventory
    def get_productPrice(self, nameProduct):
        if nameProduct in self._products:
            return self._products[nameProduct]['price']

    def get_productQuantity(self, nameProduct):
        if nameProduct in self._products:
            return self._products[nameProduct]['quantity']

    # Display the inventory contents
    def display_Inventory(self):
        for product, data in self._products.items():
            print(f"{product}, {data['price']}, {data['quantity']}")


# Define a class representing a ShoppingCart
class ShoppingCart:
    def __init__(self, buyerName, inventory):
        # Initialize the shopping cart with buyer's name, inventory reference, and an empty cart
        self._buyer_name = buyerName
        self._inventory = inventory
        self._cart = {}

    # Method to add products to the cart
    def add_to_cart(self, nameProduct, requestedQuantity):
        # Check if the requested quantity is available in the inventory
        available_quantity = self._inventory.get_productQuantity(nameProduct)
        if available_quantity >= requestedQuantity:
            # Add the product to the cart and update the inventory
            if nameProduct in self._cart:
                self._cart[nameProduct] += requestedQuantity
            else:
                self._cart[nameProduct] = requestedQuantity
            self._inventory.remove_productQuantity(nameProduct, requestedQuantity)
            return "Filled the order"
        else:
            return "Can not fill the order"

    # Method to remove products from the cart
    def remove_from_cart(self, nameProduct, requestedQuantity):
        # Check if the product is in the cart and the requested quantity can be removed
        if nameProduct in self._cart:
            if self._cart[nameProduct] >= requestedQuantity:
                # Remove the quantity from the cart and update the inventory
                self._cart[nameProduct] -= requestedQuantity
                self._inventory.add_productQuantity(nameProduct, requestedQuantity)
                return "Successful"
            else:
                return "The requested quantity to be removed from cart exceeds what is in the cart"
        else:
            return "Product not in the cart"

    # Method to view the contents of the cart
    def view_cart(self):
        total_price = 0
        for product, quantity in self._cart.items():
            # Calculate and display the total price of items in the cart
            price = self._inventory.get_productPrice(product)
            total_price += price * quantity
            print(f"{product} {quantity}")
        print(f"Total: {total_price}")
        print(f"Buyer Name: {self._buyer_name}")


# Define a class representing a ProductCatalog
class ProductCatalog:
    def __init__(self):
        # Initialize an empty set to store unique products
        self._products = set()

    # Method to add a product to the catalog
    def addProduct(self, product):
        self._products.add(product)

    # Method to categorize and display the products in the catalog by price
    def price_category(self):
        low_prices = medium_prices = high_prices = 0
        for product in self._products:
            price = product.get_price()
            if 0 <= price <= 99:
                low_prices += 1
            elif 100 <= price <= 499:
                medium_prices += 1
            elif price >= 500:
                high_prices += 1
        print(f"Number of low price items: {low_prices}")
        print(f"Number of medium price items: {medium_prices}")
        print(f"Number of high price items: {high_prices}")

    # Method to display the products in the catalog sorted by price
    def display_catalog(self):
        sorted_products = sorted(self._products, key=lambda product: product.get_price())
    
        for product in sorted_products:
            print(f"Product: {product.get_name()} Price: {product.get_price()} Category: {product.get_category()}")


# Function to populate an inventory from a file
def populate_inventory(filename):
    inventory = Inventory()
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, price, quantity, _ = map(str.strip, line.split(","))
                inventory.add_to_productInventory(name, int(price), int(quantity))
    except FileNotFoundError:
        print(f"Could not read file: {filename}")
    return inventory


# Function to populate a product catalog from a file
def populate_catalog(fileName):
    catalog = ProductCatalog()
    try:
        with open(fileName, 'r') as file:
            for line in file:
                name, price, quantity, category = map(str.strip, line.split(","))
                product = Product(name, int(price), category)
                catalog.addProduct(product)
    except FileNotFoundError:
        print(f"Could not read file: {fileName}")
    return catalog


