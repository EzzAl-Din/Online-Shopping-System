from product import Product


class BookProduct(Product):
    """
    Represents a book product in the online store.

    Attributes:
        Inherits attributes from Product:
            _name (str): The name of the book product.
            _product_id (int): The product ID of the book product.
            _price (float): The price of the book product.
        _author (str): The author of the book.
        _publisher (str): The publisher of the book.
    """

    def __init__(
        self, name: str, product_id: int, price: float, author: str, publisher: str
    ):
        """
        Initializes a new BookProduct object.

        Args:
            name (str): The name of the book product.
            product_id (int): The product ID of the book product.
            price (float): The price of the book product.
            author (str): The author of the book.
            publisher (str): The publisher of the book.
        """
        super().__init__(name + " Book", product_id, price)
        self.__author = author
        self.__publisher = publisher

    def __str__(self) -> str:
        """
        Returns a string representation of the book product.

        Returns:
            str: A string representation of the book product.
        """
        return f"Book name: {super().get_name()}, Product ID: {super().get_product_id()}, Author name:{self.__author}, Publisher name: {self.__publisher}"
