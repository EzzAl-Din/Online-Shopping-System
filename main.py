from typing import Literal
from clothing_product import ClothingProduct
from electronic_product import ElectronicProduct
from book_product import BookProduct
from customer import Customer
from address import Address
from cart import Cart
from order import Order

product_types = [
    ElectronicProduct("Smartphone", 98231, 1000, "Samsung", 1),
    ElectronicProduct("TV", 46513, 1500, "LG", 2),
    ClothingProduct("T-Shirt", 86451, 20, "Medium", "Cotton"),
    ClothingProduct("Jeans", 67892, 35, "small", "Jeans"),
    BookProduct("OOP", 79846, 60, "O'Reilly", "X Publications"),
    BookProduct("lisa", 56132, 35, "conan", "X Publications"),
]

is_positive_integer = lambda x: x.isdigit() and int(x) > 0
is_alphabetic = lambda x: x.isalpha()
is_valid_choice = lambda n: lambda x: x.isdigit() and int(x) in range(1, n + 1)

MESSAGE_INT_ERROR = "Invalid input, please enter positive numeric value."
MESSAGE_STR_ERROR = "Invalid input, please enter alphabetic characters only."
MESSAGE_CHOICE_ERROR = "Invalid choice, please enter valid choice."


def get_valid_input(prompt: str, validation_fn, error_msg: str):
    """Get valid input from the user.

    Args:
        prompt (str): The prompt to display to the user.
        validation_fn (function): The validation function to check the input.
        error_msg (str): The error message to display if input is invalid.

    Returns:
        The valid input provided by the user.
    """
    while True:
        try:
            value = input(prompt).strip()
            if value.isalpha():
                value = value.lower()
            if not validation_fn(value):
                raise ValueError(error_msg)
            return int(value) if value.isdigit() else value
        except ValueError as e:
            print(e)


def get_product_by_type(product_type: int) -> object:
    """Get product by type from the list of available product types.

    Args:
        product_type (int): The index of the product type in the list.

    Returns:
        Product: The product object corresponding to the given type.

    Raises:
        ValueError: If the product type is invalid.
    """
    try:
        return product_types[product_type]
    except IndexError:
        raise ValueError("Invalid product type")


def get_customer_address():
    """Get customer address details from the user."""
    print("Enter address:")
    area = get_valid_input("Area: ", is_alphabetic, MESSAGE_STR_ERROR)
    street_name = get_valid_input("Street name: ", is_alphabetic, MESSAGE_STR_ERROR)
    building_number = get_valid_input(
        "Building number: ", is_positive_integer, MESSAGE_INT_ERROR
    )
    apartment_number = get_valid_input(
        "Apartment number: ", is_positive_integer, MESSAGE_INT_ERROR
    )
    address = Address(area, street_name, building_number, apartment_number)
    return address


def get_customer_details():
    """This function prompts the user to input their customer ID, name, and address.

    Returns:
        tuple: A tuple containing the customer ID, name, and address.
    """
    customer_id = int(
        get_valid_input(
            "Enter your customer ID: ", is_positive_integer, MESSAGE_INT_ERROR
        )
    )
    customer_name = get_valid_input(
        "Enter your customer name: ",
        lambda x: x.replace(" ", "").isalpha(),
        MESSAGE_STR_ERROR,
    )

    customer_address = get_customer_address()

    return customer_id, customer_name, customer_address


def handle_cart_operation(cart: Cart, operation: Literal["add", "remove", "clear"]):
    """Handle add or remove or clear operations on the cart.

    Args:
        cart (Cart): The cart object to operate on.
        operation (Literal["add", "remove", "clear"]): The operation to perform.
    """
    if operation != "clear":
        print("Available products:")
        for counter, product in enumerate(product_types, 1):
            print(f"\t{counter}- {product.get_name()} {{{product.get_price()}$}}")
        flag = get_valid_input(
            f"How many products you want to {operation} ?: ",
            is_positive_integer,
            MESSAGE_INT_ERROR,
        )
        while flag > 0:
            product_type = get_valid_input(
                "Enter Your Product Type: ", is_positive_integer, MESSAGE_INT_ERROR
            )
            try:
                product = get_product_by_type(product_type - 1)
                if operation == "add":
                    cart.add_product(product)
                elif operation == "remove":
                    cart.remove_product(product)
                flag -= 1
            except ValueError as e:
                print(f"Error: {e} Please enter a valid choice.")
    else:
        cart.clear_cart()


def main():
    """Main function to run the program."""
    while True:
        new_customer = True
        if new_customer == True:
            customer_id, customer_name, customer_address = get_customer_details()
            customer = Customer(customer_id, customer_name, customer_address)

        cart = Cart()

        handle_cart_operation(cart, "add")

        while True:
            total = cart.calculate_total_price()

            flag = get_valid_input(
                f"Your total is ${total:.2f}. Would you like to place the order? (1-yes 2-no): ",
                is_valid_choice(2),
                MESSAGE_CHOICE_ERROR,
            )
            if flag == 1:
                order = Order(cart, customer)
                order.set_order_status("confirmed")
                order.print_order_info()
                break
            else:
                action = get_valid_input(
                    "Would you like to (1-add product, 2-remove product, 3-clear cart, 4-cancel order)? ",
                    is_valid_choice(4),
                    MESSAGE_CHOICE_ERROR,
                )
                if action == 1:
                    handle_cart_operation(cart, "add")
                elif action == 2:
                    handle_cart_operation(cart, "remove")
                elif action == 3:
                    handle_cart_operation(cart, "clear")
                    handle_cart_operation(cart, "add")
                else:
                    print("The order has been cancelled.")
                    break
        new_order_flag = get_valid_input(
            "Would you like to make a new order? (1-yes 2-no): ",
            is_valid_choice(2),
            MESSAGE_CHOICE_ERROR,
        )
        if new_order_flag == 1:

            new_order_flag = get_valid_input(
                "Is the order for the same customer? (1-yes 2-no): ",
                is_valid_choice(2),
                MESSAGE_CHOICE_ERROR,
            )
            if new_order_flag == 1:
                new_customer = False
        else:
            break


if __name__ == "__main__":
    main()
