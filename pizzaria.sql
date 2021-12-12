CREATE DATABASE pizzaria;


USE pizzaria;


CREATE TABLE cadastros(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome varchar(50) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    nivel INT NOT NULL
);


INSERT INTO cadastros(nome, senha, nivel)
VALUES('admin', 'admin', 2);


INSERT INTO cadastros(nome, senha, nivel)
VALUES('laura', '123', 1);


SELECT *
FROM cadastros;


CREATE TABLE produtos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    grupo VARCHAR(100),
    ingredientes VARCHAR(1000),
    preco FLOAT
);


INSERT INTO produtos(nome, ingredientes, grupo, preco)
VALUES (
        "Pizza de calabresa",
        "Calabresa, Tomate, Queijo",
        "Pizzas",
        34.9
    );

INSERT INTO produtos(nome, ingredientes, grupo, preco)
VALUES (
        "Coca cola",
        "",
        "Bebidas",
        7
    );

INSERT INTO produtos(nome, ingredientes, grupo, preco)
VALUES (
        "Pizza de Muçarela",
        "Muçarela, Molho de tomate",
        "Pizzas",
        34.9
    );

SELECT *
FROM produtos;


CREATE TABLE pedidos(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ingredientes VARCHAR(1000),
    grupo VARCHAR(100),
    localEntrega VARCHAR(500),
    observacoes VARCHAR(1000)
);


INSERT INTO pedidos (
        nome,
        ingredientes,
        grupo,
        localEntrega,
        observacoes
    )
VALUES (
        'Pizza de Muçarela',
        'Muçarela, Molho de tomate',
        'Pizzas',
        '',
        'Sem cebola'
    );


INSERT INTO pedidos(
        nome,
        ingredientes,
        grupo,
        localEntrega,
        observacoes
    )
VALUES ('Coca cola', '', 'Bebidas', '', '');


SELECT *
FROM pedidos;


CREATE TABLE estatisticaVendido(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    grupo varchar(100),
    preco float
);

SELECT *
FROM estatisticaVendido;