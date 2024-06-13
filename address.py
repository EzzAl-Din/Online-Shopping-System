class Address:
    """
    Represents an address in the online shopping system.

    Attributes:
        _area (str): The area of the address.
        _street_name (str): The street name of the address.
        _building_number (int): The building number of the address.
        _apartment_number (int): The apartment number of the address.
    """
    def __init__(
        self, area: str, street_name: str, building_number: int, apartment_number: int
    ):
        """
        Constructor for the Address class.

        Args:
            area (str): The area of the address.
            street_name (str): The street name of the address.
            building_number (int): The building number of the address.
            apartment_number (int): The apartment number of the address.
        """
        self.__area = area
        self.__street_name = street_name
        self.__building_number = building_number
        self.__apartment_number = apartment_number

    def __str__(self):
        """
        Returns a string representation of the address.

        Returns:
            str: A string representation of the address.
        """
        return f"Apartment No. {self.__apartment_number} Building No. {self.__building_number} {self.__street_name} Street {self.__area} area"
