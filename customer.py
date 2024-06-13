from address import Address


class Customer:
    """
    Represents a customer in the online shopping system.

    Attributes:
        _customer_id (int): The ID of the customer.
        _name (str): The name of the customer.
        _address (Address): An Address object representing the customer's address.
    """

    def __init__(self, customer_id: int, name: str, address: Address):
        """
        Constructor for the Customer class.

        Args:
            customer_id (int): The ID of the customer.
            name (str): The name of the customer.
            address (Address): An Address object representing the customer's address.
        """
        self.__customer_id = abs(customer_id)
        self.__name = name
        self.__address = address

    def __str__(self):
        """
        Returns a string representation of the customer.

        Returns:
            str: A string representation of the customer.
        """
        return f"Customer ID: {self.__customer_id}, Name: {self.__name}, Address: {self.__address}"

    def get_customer_id(self) -> int:
        """
        Get the ID of the customer.

        Returns:
            int: The ID of the customer.
        """
        return self.__customer_id

    def get_customer_name(self) -> str:
        """
        Get the name of the customer.

        Returns:
            str: The name of the customer.
        """
        return self.__name

    def get_customer_address(self) -> Address:
        """
        Get the address of the customer.

        Returns:
            Address: An Address object representing the customer's address.
        """
        return self.__address
