from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    """
    Abstract base class representing a product in the online store.

    Attributes:
        _name (str): The name of the product.
        _product_id (int): The product ID.
        _price (float): The price of the product.
    """

    def __init__(self, name: str, product_id: int, price: float):
        """
        Initializes a new Product object.

        Args:
            name (str): The name of the product.
            product_id (int): The product ID.
            price (float): The price of the product.
        """
        self.__name = name
        self.__product_id = abs(product_id)
        self.__price = abs(price)

    @abstractmethod
    def __str__(self) -> str:
        """
        Abstract method to return a string representation of the product.

        Returns:
            str: A string representation of the product.
        """
        pass

    def get_name(self) -> str:
        """
        Get the name of the product.

        Returns:
            str: The name of the product.
        """
        return self.__name

    def get_product_id(self) -> int:
        """
        Get the product ID.

        Returns:
            int: The product ID.
        """
        return self.__product_id

    def get_price(self) -> float:
        """
        Get the price of the product.

        Returns:
            float: The price of the product.
        """
        return self.__price
