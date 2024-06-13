from product import Product


class ElectronicProduct(Product):
    """
    Represents an electronic product in the online store.

    Attributes:
        Inherits attributes from Product:
            _name (str): The name of the electronic product.
            _product_id (int): The product ID of the electronic product.
            _price (float): The price of the electronic product.
        _brand (str): The brand of the electronic product.
        _warranty_period (int): The warranty period of the electronic product.
    """

    def __init__(
        self, name: str, product_id: int, price: float, brand: str, warranty_period: int
    ):
        """
        Initializes a new ElectronicProduct object.

        Args:
            name (str): The name of the electronic product.
            product_id (int): The product ID of the electronic product.
            price (float): The price of the electronic product.
            brand (str): The brand of the electronic product.
            warranty_period (int): The warranty period of the electronic product.
        """
        super().__init__(name, product_id, price)
        self.__brand = brand
        self.__warranty_period = abs(warranty_period)

    def __str__(self) -> str:
        """
        Returns a string representation of the electronic product.

        Returns:
            str: A string representation of the electronic product.
        """
        return f"Product name: {super().get_name()}, Product ID: {super().get_product_id()}, Brand name:{self.__brand}, Warranty period: {self.__warranty_period}"
