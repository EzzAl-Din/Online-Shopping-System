from product import Product


class Cart:
    """
    Represents a shopping cart in the online store.

    Attributes:
        __products (list): A list to hold Product objects in the cart.
    """
    def __init__(self):
        """
        Constructor for the Cart class.
        Creates an empty list to hold Product objects
        """
        self.__products: list[Product] = []

    def __str__(self):
        """
        Returns a string representation of the cart, listing the names of all products in the cart.
        """
        product_details = [product.get_name() for product in self.__products]
        return f"Products: {', '.join(product_details)}"

    def get_nProducts(self) -> int:
        """
        Returns the number of products in the cart.
        """
        return len(self.__products)

    def add_product(self, product: Product) -> None:
        """
        Adds a product object to the cart.
        """
        self.__products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Removes a product object from the cart.
        Raises:
                ValueError: If the product is not in the cart.
        """
        if product in self.__products:
            self.__products.remove(product)
        else:
            raise ValueError("Product not in cart.")

    def clear_cart(self):
        """
        Clears all products from the cart.
        """
        self.__products = []

    def get_products(self) -> list:
        """
        Returns a list of all products in the cart.
        """
        return self.__products

    def calculate_total_price(self) -> float:
        """
        Calculates the total price of all products in the cart.
        """
        return sum(product.get_price() for product in self.__products)
