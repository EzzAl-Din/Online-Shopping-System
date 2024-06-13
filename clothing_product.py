from product import Product


class ClothingProduct(Product):
    """
    Represents a clothing product in the online store.

    Attributes:
        Inherits attributes from Product:
            _name (str): The name of the clothing product.
            _product_id (int): The product ID of the clothing product.
            _price (float): The price of the clothing product.
        _size (str): The size of the clothing product.
        _fabric (str): The fabric of the clothing product.
    """

    def __init__(
        self, name: str, product_id: int, price: float, size: str, fabric: str
    ):
        """
        Initializes a new ClothingProduct object.

        Args:
            name (str): The name of the clothing product.
            product_id (int): The product ID of the clothing product.
            price (float): The price of the clothing product.
            size (str): The size of the clothing product.
            fabric (str): The fabric of the clothing product.
        """
        super().__init__(name, product_id, price)
        self.__size = size
        self.__fabric = fabric

    def __str__(self) -> str:
        """
        Returns a string representation of the clothing product.

        Returns:
            str: A string representation of the clothing product.
        """
        return f"Product name: {super().get_name()}, Product ID: {super().get_product_id()}, Size:{self.__size}, Fabric: {self.__fabric}"
