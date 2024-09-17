# Online Shopping System

## Overview

This project is a Python-based online shopping system that demonstrates my proficiency in Object-Oriented Programming (OOP).<br>
The system incorporates classes to manage products, customers, and orders, showcasing the use of OOP principles.<br>
Users can interact with various product types, manage a shopping cart, and place orders through a user-friendly interface.<br>
By employing OOP techniques, the system is designed with modularity and scalability in mind, allowing for efficient code organization and<br> ease of maintenance.

## Features

- **Product Management**: Define and manage different types of products including books, clothing, and electronics.
- **Shopping Cart**: Add, remove, and clear products from the cart. Calculate the total price of the cart.
- **Customer Management**: Input and store customer details including address.
- **Order Management**: Place orders with unique IDs, track order status, and print order details.

## Classes

- **`Product`**: Abstract base class for all product types. Attributes include `name`, `product_id`, and `price`.
- **`BookProduct`**: Inherits from `Product`. Additional attributes: `author` and `publisher`.
- **`ClothingProduct`**: Inherits from `Product`. Additional attributes: `size` and `fabric`.
- **`ElectronicProduct`**: Inherits from `Product`. Additional attributes: `brand` and `warranty_period`.
- **`Address`**: Represents a customer’s address with attributes like `area`, `street_name`, `building_number`, and `apartment_number`.
- **`Customer`**: Represents a customer with attributes `customer_id`, `name`, and `address`.
- **`Cart`**: Manages a list of `Product` objects. Provides methods to add, remove, and clear products, as well as calculate the total price.
- **`Order`**: Manages orders with attributes such as `order_id`, `cart`, `customer`, and `order_status`.
   
## Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/online-shopping-system.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd online-shopping-system
    ```

3. **Run the main program**:
    ```bash
    python main.py
    ```

## Usage

- The system will prompt for customer details including address.
- Users can perform operations on the cart (add, remove, clear products).
- Place an order and view the order details including total price and product information.

## Requirements

- Python 3.x

## Contributing

Feel free to open issues or submit pull requests to improve the project.

## Contact

For any questions or feedback, please contact [ezzaldinaref@gmail.com](mailto:ezzaldinaref@gmail.com).
