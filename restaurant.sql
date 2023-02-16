CREATE DATABASE pizzaRestaurant;


USE pizzaRestaurant;


CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(50) NOT NULL,
    password VARCHAR(20) NOT NULL,
    level INT NOT NULL
);


INSERT INTO users(name, password, level)
VALUES('admin', 'admin', 2);


INSERT INTO users(name, password, level)
VALUES('laura', '123', 1);


SELECT *
FROM users;



CREATE TABLE products(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    prodGroup VARCHAR(100),
    ingredients VARCHAR(1000),
    price FLOAT
);


INSERT INTO products(name, ingredients, prodGroup, price)
VALUES (
        "Pepperoni Pizza",
        "Pepperoni, Tomato, Cheese",
        "Pizzas",
        34.9
    );

INSERT INTO products(name, ingredients, prodGroup, price)
VALUES (
        "Coca cola",
        "",
        "Drinks",
        7
    );

INSERT INTO products(name, ingredients, prodGroup, price)
VALUES (
        "Mozzarella Pizza",
        "Mozzarella, Tomato Sauce",
        "Pizzas",
        34.9
    );


SELECT *
FROM products;


CREATE TABLE orders(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    ingredients VARCHAR(1000),
    orderGroup VARCHAR(100),
    deliveryAddress VARCHAR(500),
    notes VARCHAR(1000)
);


INSERT INTO orders (
        name,
        ingredients,
        orderGroup,
        deliveryAddress,
        notes
    )
VALUES (
        'Mozzarella Pizza',
        'Mozzarella, Tomato Sauce',
        'Pizzas',
        '',
        'No onions'
    );


INSERT INTO orders(
        name,
        ingredients,
        orderGroup,
        deliveryAddress,
        notes
    )
VALUES ('Coca cola', '', 'Drinks', '', '');


SELECT *
FROM orders;


CREATE TABLE soldStatistics(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    statsGroup varchar(100),
    price float
);

SELECT *
FROM soldStatistics;