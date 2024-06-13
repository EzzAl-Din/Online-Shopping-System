import datetime
from typing import Literal
from cart import Cart
from customer import Customer


class Order:
    """
    Represents an order placed by a customer in the online store.

    Attributes:
        __order_counter (int): A counter to generate unique order IDs.
        __last_time (str): A string representing the last time an order was generated.
        __order_id (int): The unique ID of the order.
        __cart (Cart): The cart associated with the order.
        __customer (Customer): The customer who placed the order.
        __order_status (str): The status of the order (active, confirmed, cancelled).
    """

    __order_counter = 0
    __last_time = None

    @classmethod
    def __generate_id(cls):
        """
        Generates a unique order ID based on the current date and time.

        Returns:
            str: A unique order ID.
        """
        now = datetime.datetime.now()
        current_time_str = now.strftime("%Y%m%d%H%M")

        # Reset the counter if the current minute has changed
        if cls.__last_time != current_time_str:
            cls.__order_counter = 1
            cls.__last_time = current_time_str
        else:
            cls.__order_counter += 1

        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        # Format the ID as YYYYMMDDHHMMXX where XX is the counter
        id = f"{year}{month:02}{day:02}{hour:02}{minute:02}{cls.__order_counter:02}"
        return id

    def __init__(self, cart: Cart, customer: Customer):
        """
        Constructor for the Order class.

        Args:
            cart (Cart): The cart associated with the order.
            customer (Customer): The customer who placed the order.
        """
        self.__order_id = int(Order.__generate_id())
        self.__cart = cart
        self.__customer = customer
        self.__order_status = "active"  # Default status is active

    def set_order_status(self, status: Literal["confirmed", "cancelled"]):
        """
        Sets the status of the order.

        Args:
            status (Literal["confirmed", "cancelled"]): The new status of the order.
        """
        self.__order_status = status

    def print_order_info(self) -> None:
        """
        Print information about the order.
        """
        print(f"Order Status: {self.__order_status}")
        print(f"Order ID: {self.__order_id}")
        print(f"Customer ID: {self.__customer.get_customer_id()}")
        print(f"Customer Name: {self.__customer.get_customer_name()}")
        print(f"Customer Address: {self.__customer.get_customer_address()}")
        print(f"Total number of products: {self.__cart.get_nProducts()}")
        print(f"Products:")
        for count, product in enumerate(self.__cart.get_products(), 1):
            print(f"\t{count} - {product.get_name()} - ${product.get_price():.2f}")
        print(f"Total: {self.__cart.calculate_total_price():.2f}$")
